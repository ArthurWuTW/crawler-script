import cv2
import numpy as np
import math


plants = [
    {
        "id":1,
        "seed_num":1,
        "center_pt": tuple([123, 456]),
        "edge_pt": tuple([333, 333])
    },
    {
        "id":2,
        "seed_num":2,
        "center_pt": tuple([123, 456]),
        "edge_pt": tuple([333, 333])
    },
    {
        "id":3,
        "seed_num":1,
        "center_pt": tuple([123, 456]),
        "edge_pt": tuple([333, 333])
    }

]

# Create the threshold image
img = cv2.imread("./abc.jpg")
img = cv2.GaussianBlur(img, (3,3), 0)
b, g, r = cv2.split(img)
ret, thresh = cv2.threshold(g, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("123", g)
cv2.waitKey(0)

for plant in plants:
    print(plant)

    # Create mask image
    radius = int(math.sqrt((plant['center_pt'][0]-plant['edge_pt'][0])**2+(plant['center_pt'][1]-plant['edge_pt'][1])**2))
    center = plant['center_pt']

    size = g.shape
    mask = np.zeros(size, np.uint8)
    cv2.circle(mask, center, radius, (255, 255, 255), -1)

    cv2.imshow("123", mask)
    cv2.waitKey(0)

    # Bitwise_and
    result = cv2.bitwise_and(thresh, thresh, mask=mask)
    cv2.imshow("123", result)
    cv2.waitKey(0)

    # Calculate Percentage
    nonzero_count = cv2.countNonZero(result)
    print(nonzero_count)

    circle_area = 3.14*radius**2

    print(nonzero_count/circle_area)
