import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

height, width, channels = frame.shape

print(height, width, channels)

print(frame)

import base64
import numpy as np

base64_str = cv2.imencode('.jpg', frame)[1].tostring()

print(base64_str)

base64_str = base64.b64encode(base64_str)

print(base64_str)

print("-----------------decode utf-8---------")
print(base64_str.decode("utf-8"))


imgString = base64.b64decode(base64_str)
nparr = np.fromstring(imgString, np.uint8)
image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

print(image)
