import RPi.GPIO as GPIO
import time
import requests
import os
import json
GPIO_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)

secret_data_path = os.path.dirname(os.path.abspath(__file__))+"/secret_data.json"
secret_data = None
with open(secret_data_path, "r") as file:
    secret_data = json.load(file)
print(secret_data)

try:
    while True:
        print('on')
        GPIO.output(GPIO_PIN, GPIO.HIGH)
        time.sleep(60)
        print('off')
        GPIO.output(GPIO_PIN, GPIO.LOW)
        #time.sleep(5)
        ip = "https://plantmonitor.mooo.com"
        # log message
        data = {
                'raspberry_secret_key': secret_data['raspberry_secret_key'],
                'title': "PUMP",
                'msg': "[Pump] Watering done",
                'type': "LOG"
        }
        headers = {'content-type': 'application/json'}
        r = requests.post(ip+'/writeLogMessage', data=json.dumps(data), headers=headers)
        data = {
                'raspberry_secret_key': secret_data['raspberry_secret_key'],
                'status': "Done"
        }
        headers = {'content-type': 'application/json'}
        r = requests.post('https://plantmonitor.mooo.com/updateWateringStatus', data=json.dumps(data), headers=headers)
        #r = requests.get(ip+"/updateWateringStatus/Done")
        break
except KeyboardInterrupt:
    print('aaa')
finally:
    GPIO.cleanup()
