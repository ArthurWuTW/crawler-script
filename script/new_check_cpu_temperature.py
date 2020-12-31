import re, subprocess
import requests
import time
import os
import json

secret_data_path = os.path.dirname(os.path.abspath(__file__))+"/secret_data.json"
secret_data = None
with open(secret_data_path, "r") as file:
    secret_data = json.load(file)
print(secret_data)


def check_CPU_temp():
    temp = None
    err, msg = subprocess.getstatusoutput('vcgencmd measure_temp')
    if not err:
        m = re.search(r'-?\d\.?\d*', msg)
        try:
            temp = float(m.group())
        except:
            pass
    return temp, msg

while True:
    temp, msg = check_CPU_temp()
    print(temp)

    ip = "https://plantmonitor.mooo.com"
    #data = "/updatePiCpuTemperature/"+str(temp).replace(".", "%2E")+"%20%2a7C"

    try:
        # Post data
        data = {
                'raspberry_secret_key': secret_data['raspberry_secret_key'],
                'status': str(temp)+" 'C"
        }
        print(data)
        headers = {'content-type': 'application/json'}
        r = requests.post(ip+'/updatePiCpuTemperature', data=json.dumps(data), headers=headers)
    except:
        pass
    
    break
    #time.sleep(60)
