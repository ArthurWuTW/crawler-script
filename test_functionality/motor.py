import RPi.GPIO as GPIO
import time
 
In1, In2 = 9, 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)

def initial_gpio():
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.LOW)

def forward():
    GPIO.output(In1, GPIO.HIGH)
    GPIO.output(In2, GPIO.LOW)

def backward():
    GPIO.output(In2, GPIO.HIGH)
    GPIO.output(In1, GPIO.LOW)

import cv2
from cv2 import aruco

def arucoCenterDetection(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    
    center_points_dict_array = list()
    for i in range(len(ids)):
        c = corners[i][0]
        #if(ids[i][0]==1):
        #    print(c)
        if(len(c[:, 0])==4):
            center_point = dict()
            center_point['id'] = ids[i][0]
            center_point['center_point'] = [c[:, 0].mean(), c[:, 1].mean()]
            center_points_dict_array.append(center_point)
    
    return center_points_dict_array


#capturing = cv2.VideoCapture(0)
initial_gpio()

def get_image_frame():
    _, frame = capturing.read()
    return frame

count = 0

try:
    while True:

        capturing = None

        capturing = cv2.VideoCapture(0)

        image = get_image_frame()
        #print(image.shape)
        center_point_array = arucoCenterDetection(image)
        #print(center_point_array)

        for center_points in center_point_array:
            if(center_points['id'] == 1):
                print("id is 1!")

                if(center_points['center_point'][0] < 320):
                    print("left side!")
                    print(center_points['center_point'])
                    backward()
                    time.sleep(0.3)
                    initial_gpio()
                elif(center_points['center_point'][0] > 320):
                    print("right side")
                    print(center_points['center_point'])
                    forward()
                    time.sleep(0.5)
                    initial_gpio()
                break
        #print('forward')
        #forward()
        #time.sleep(5)
        #print('backward')
        #backward()
        #time.sleep(5)
except KeyboardInterrupt:
    print('aaa')
finally:
    GPIO.cleanup()
