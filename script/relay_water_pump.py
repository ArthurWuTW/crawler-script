import RPi.GPIO as GPIO
import time
import requests
GPIO_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)
 
try:
    while True:
        print('on')
        GPIO.output(GPIO_PIN, GPIO.HIGH)
        time.sleep(60)
        print('off')
        GPIO.output(GPIO_PIN, GPIO.LOW)
        #time.sleep(5)
        ip = "http://10.1.1.2:8000"
        r = requests.get(ip+"/writeLogMessage/PUMP/%5BPUMP%5D%20Pump%20Watering%20Done/LOG")
        r = requests.get(ip+"/updateWateringStatus/Done")
        break
except KeyboardInterrupt:
    print('aaa')
finally:
    GPIO.cleanup()
