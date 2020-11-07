import RPi.GPIO as GPIO
import time
import cv2
from cv2 import aruco
import base64
import json
import requests

class Motor():
    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.gpio = GPIO
        self.gpio.setmode(GPIO.BCM)
        self.gpio.setup(self.input1, GPIO.OUT)
        self.gpio.setup(self.input2, GPIO.OUT)
        self.maxStep = 200

    def stop(self):
        self.gpio.output(self.input1, GPIO.LOW)
        self.gpio.output(self.input2, GPIO.LOW)

    def forward(self, second):
        self.gpio.output(self.input1, GPIO.HIGH)
        self.gpio.output(self.input2, GPIO.LOW)
        time.sleep(second)
        self.stop()

    def backward(self, second):
        self.gpio.output(self.input2, GPIO.HIGH)
        self.gpio.output(self.input1, GPIO.LOW)
        time.sleep(second)
        self.stop()

class ImageGrabber():
    def __init__(self, id):
        self.grabber = cv2.VideoCapture(id)

    def resetCapturingConfiguration(self, id):
        self.grabber = None
        self.grabber = cv2.VideoCapture(id)

    def getImageFrame(self):
        _, frame = self.grabber.read()
        return frame

class ArucoLibrary():
    def __init__(self):
        self.ARUCO = aruco

    def detectArucoCorner(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        aruco_dict = self.ARUCO.Dictionary_get(aruco.DICT_6X6_250)
        parameters =  self.ARUCO.DetectorParameters_create()
        corners, ids, _ = self.ARUCO.detectMarkers(gray, aruco_dict, parameters=parameters)
        return corners, ids

    def getCenterPoints(self, corners, ids):
        centerPoints = list()
        print(ids)
        if ids is not None:
            for i in range(len(ids)):
                c = corners[i][0]
                if(len(c[:, 0]) == 4):
                    centerPoint = dict()
                    centerPoint['id'] = ids[i][0]
                    centerPoint['x'] = c[:, 0].mean()
                    centerPoint['y'] = c[:, 1].mean()
                    centerPoints.append(centerPoint)
        return centerPoints

class ImagePoster():
    def __init__(self, url):
        self.url = url
    def postImageArucoid(self, image, id):
        base64_str = cv2.imencode('.jpg', image)[1].tostring()
        base64_str = base64.b64encode(base64_str)
        base64_str_decod_utf_8 = base64_str.decode("utf-8")
        data = {
            'id': id,
            'image': base64_str_decod_utf_8,
        }
        headers = {'content-type': 'application/json'}
        r = requests.post(self.url, data=json.dumps(data), headers=headers)

if __name__ == '__main__':
    motor = Motor(9, 10)
    motor.stop()
    imageGrabber = ImageGrabber(0)
    arucoLib = ArucoLibrary()
    ip = "http://10.1.1.16:8000/receiveImage"
    imagePoster = ImagePoster(ip)

    arucoAllArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    arucoIdArray = [1, 3, 5, 7, 9, 11]

    try:
        for id in arucoAllArray:
            moveCount = 0
            while True:
                # TODO bugfix: error message - Corrupt JPEG data: 1 extraneous bytes before marker 0xd6
                # reseting VideoCapture can fix it, but it slows down the whole process
                imageGrabber.resetCapturingConfiguration(0)
                image = imageGrabber.getImageFrame()
                _, width, _ = image.shape
                cornersArray, idsArray = arucoLib.detectArucoCorner(image)
                centerPointsArray = arucoLib.getCenterPoints(cornersArray, idsArray)

                accurateFlag = False
                passFlag = False

                for center in centerPointsArray:
                    if(center['id'] == id):
                        print(center['x'], center['y'])
                        moveCount += 1
                        if(center['x'] < width/2):
                            motor.backward(0.6)
                        elif(center['x'] > width/2):
                            motor.forward(0.6)

                        if(abs(center['x'] - width/2) <= 5):
                            if center['id'] in arucoIdArray:
                                accurateFlag = True
                            else:
                                passFlag = True
                        break

                if(passFlag):
                    break

                if(accurateFlag):
                    imagePoster.postImageArucoid(image, id)
                    break
                
                if(moveCount == motor.maxStep):
                    raise Exception("reach MaxStep, system shutdown!")
        motor.maxStep = 50
        count = 0
        while True:
            imageGrabber.resetCapturingConfiguration(0)
            image = imageGrabber.getImageFrame()
            _, width, _ = image.shape
            cornersArray, idsArray = arucoLib.detectArucoCorner(image)
            centerPointsArray = arucoLib.getCenterPoints(cornersArray, idsArray)
            sortedCenterPointsArray = sorted(centerPointsArray, key=lambda k: k['id'])
            if sortedCenterPointsArray is not None:
              backCenterPoint = sortedCenterPointsArray[0]
              print(backCenterPoint['id'], backCenterPoint['x'], backCenterPoint['y'])
              if(backCenterPoint['x'] < width/2):
                  motor.backward(0.6)
              elif(backCenterPoint['x'] > width/2):
                  motor.forward(0.6)

              if(backCenterPoint['id'] == arucoIdArray[0]):
                  count += 1
                  print(count)
                  if(count == motor.maxStep):
                      break
            
              if(backCenterPoint['id'] == arucoIdArray[0] and abs(backCenterPoint['x'] - width/2) <= 5):
                  print("less than two, move to next id")
                  break


    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        motor.gpio.cleanup()
