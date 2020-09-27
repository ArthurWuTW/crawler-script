import cv2

img = cv2.imread("./abc.jpg")

# Preprocessing
#img = cv2.medianBlur(img, 5)
img = cv2.GaussianBlur(img, (3,3), 0)

b, g, r = cv2.split(img)

# Thresholding
ret, thresh = cv2.threshold(g, 127, 255, cv2.THRESH_BINARY)



cv2.imshow("123", thresh)
cv2.waitKey(0)

ret, thresh = cv2.threshold(r, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("123", thresh)
cv2.waitKey(0)

import numpy as np
import math
size = g.shape
mask = np.zeros(size, np.uint8)

center = (367,421)
point2 = (397,361)
radius = int(math.sqrt((center[0]-point2[0])**2+(center[1]-point2[1])**2))

cv2.circle(mask, center, radius, (255,255,255), -1)

print(mask.shape)
cv2.imshow("123", mask)
cv2.waitKey(0)

res = cv2.bitwise_and(thresh, thresh, mask=mask)
cv2.imshow("123", res)
cv2.waitKey(0)

nonzero = cv2.countNonZero(res)
print(nonzero)
circle_area = 3.14*radius**2

print(nonzero/circle_area)






