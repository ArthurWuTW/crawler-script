import requests

while True:

    ip = "http://10.1.1.16:8000/"
    r = requests.get(ip+"updateCameraTask/0%25")
    r = requests.get(ip+"updateWarningCount/0")
    r = requests.get(ip+"updateWateringStatus/UNDONE")

    break
    

