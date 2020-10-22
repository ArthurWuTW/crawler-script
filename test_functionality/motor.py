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

try:
    for i in [4, 3, 2, 1]:
        count = 0
        print(i)
        while True:
            capturing = None
            capturing = cv2.VideoCapture(0)
            image = get_image_frame()
            center_point_array = arucoCenterDetection(image)
            for center_points in center_point_array:
                if(center_points['id'] == i):
                    count += 1
                    if(center_points['center_point'][0] < 320):
                        print("left")
                        backward()
                        time.sleep(0.3)
                        initial_gpio()
                    elif(center_points['center_point'][0] > 320):
                        print("right")
                        forward()
                        time.sleep(0.5)
                        initial_gpio()
                    break
            if(count == 60):
                break
except KeyboardInterrupt:
    print('aaa')
finally:
    GPIO.cleanup()
