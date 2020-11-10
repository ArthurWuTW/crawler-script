import RPi.GPIO as GPIO
import time
 
GPIO_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)
 
try:
    while True:
        print('on')
        GPIO.output(GPIO_PIN, GPIO.HIGH)
        time.sleep(8)
        print('off')
        GPIO.output(GPIO_PIN, GPIO.LOW)
        #time.sleep(5)
        ip = "http://10.1.1.16:8000"
        r = requests.get(ip+"/writeLogMessage/PUMP/%5BPUMP%5D%20Pump%20Watering%20Done/LOG")
        break
except KeyboardInterrupt:
    print('aaa')
finally:
    GPIO.cleanup()
