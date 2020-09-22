import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

height, width, channels = frame.shape

print(height, width, channels)

print(frame)
