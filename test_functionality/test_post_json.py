import cv2
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
height, width, channels = frame.shape
print(height, width, channels)
print(frame)

import base64
import numpy as np
base64_str = cv2.imencode('.jpg', frame)[1].tostring()
base64_str = base64.b64encode(base64_str)

base64_str_decod_utf_8 = base64_str.decode("utf-8")


import json
import requests

url = 'http://10.1.1.16:8000/receiveImage'
data = {
        'image': base64_str_decod_utf_8
        }

print(data)

headers = {'content-type': 'application/json'}

print(headers)

r = requests.post(url, data=json.dumps(data), headers=headers)

print("response text", r.text)


