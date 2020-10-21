import RPi.GPIO as GPIO
import time
 
In1, In2 = 6, 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)

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

        center_point = dict()
        center_point['id'] = ids[i][0]
        center_point['center_point'] = [c[:, 0].mean(), c[:, 1].mean()]
        center_points_dict_array.append(center_point)
    
    return center_points_dict_array


capturing = cv2.VideoCapture(0)

def get_image_frame():
    _, frame = capturing.read()
    return frame

try:
    while True:

        image = get_image_frame()
        print(image.shape)
        center_point_array = arucoCenterDetection(image)
        print(center_point_array)

        #print('forward')
        #forward()
        #time.sleep(5)
        #print('backward')
        #backward()
        #time.sleep(5)
        break
except KeyboardInterrupt:
    print('aaa')
finally:
    GPIO.cleanup()
