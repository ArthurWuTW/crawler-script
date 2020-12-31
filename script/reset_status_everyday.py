import requests
import json
import os
secret_data_path = os.path.dirname(os.path.abspath(__file__))+"/secret_data.json"
secret_data = None
with open(secret_data_path, "r") as file:
    secret_data = json.load(file)
print(secret_data)

while True:

    ip = "https://plantmonitor.mooo.com/"
    #r = requests.get(ip+"updateCameraTask/0%25")
    #r = requests.get(ip+"updateWarningCount/0")
    #r = requests.get(ip+"updateWateringStatus/UNDONE")
    data = {
            'raspberry_secret_key': secret_data['raspberry_secret_key'],
            'status': "0%"
    }
    headers = {'content-type': 'application/json'}
    r = requests.post('https://plantmonitor.mooo.com/updateCameraTask', data=json.dumps(data), headers=headers)
    data = {
            'raspberry_secret_key': secret_data['raspberry_secret_key'],
            'status': "0"
    }
    headers = {'content-type': 'application/json'}
    r = requests.post('https://plantmonitor.mooo.com/updateWarningCount', data=json.dumps(data), headers=headers)
    data = {
            'raspberry_secret_key': secret_data['raspberry_secret_key'],
            'status': "Undone"
    }
    headers = {'content-type': 'application/json'}
    r = requests.post('https://plantmonitor.mooo.com/updateWateringStatus', data=json.dumps(data), headers=headers)

    
    
    
    
    
    break
    

