import requests

while True:

    ip = "https://plantmonitor.mooo.com/"
    r = requests.get(ip+"updateCameraTask/0%25")
    r = requests.get(ip+"updateWarningCount/0")
    r = requests.get(ip+"updateWateringStatus/UNDONE")

    break
    

