import cv2
import math
import numpy as np
import time

def Growth_Estimate(img):
    data = list()
    plants = [
        {
            "id":1,
            "seed_num":1,
            "center_pt": tuple([366, 425]),
            "edge_pt": tuple([362, 363])
        },
        {
            "id":2,
            "seed_num":2,
            "center_pt": tuple([360, 235]),
            "edge_pt": tuple([355, 296])
        },
        {
            "id":3,
            "seed_num":1,
            "center_pt": tuple([353, 72]),
            "edge_pt": tuple([343, 118])
        }

    ]
    img = cv2.GaussianBlur(img, (3,3), 0)
    b, g, r = cv2.split(img)
    ret, thresh = cv2.threshold(g, 100, 255, cv2.THRESH_BINARY)

    for plant in plants:
        print(plant)

        # Create mask image
        radius = int(math.sqrt((plant['center_pt'][0]-plant['edge_pt'][0])**2+(plant['center_pt'][1]-plant['edge_pt'][1])**2))
        center = plant['center_pt']

        size = g.shape
        mask = np.zeros(size, np.uint8)
        cv2.circle(mask, center, radius, (255, 255, 255), -1)

        # Bitwise_and
        result = cv2.bitwise_and(thresh, thresh, mask=mask)

        # Calculate Percentage
        print("result shape", result.shape)
        nonzero_count = cv2.countNonZero(result)
        print(nonzero_count)

        circle_area = cv2.countNonZero(mask)
        print(nonzero_count/float(circle_area))

        data.append({
            "id": plant['id'],
            "growth_rate": nonzero_count/float(circle_area)
        })

    return data

while(True):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    growth_data = Growth_Estimate(frame)


    print("growth_data", growth_data)

    height, width, channels = frame.shape
    print(height, width, channels)
    print(frame)

    import base64
    base64_str = cv2.imencode('.jpg', frame)[1].tostring()
    base64_str = base64.b64encode(base64_str)

    base64_str_decod_utf_8 = base64_str.decode("utf-8")


    import json
    import requests

    url = 'http://10.1.1.16:8000/receiveImage'
    data = {
            'image': base64_str_decod_utf_8,
            'data': tuple(growth_data)
            }

    print(data)

    headers = {'content-type': 'application/json'}

    print(headers)

    r = requests.post(url, data=json.dumps(data), headers=headers)

    time.sleep(60*60*24)
