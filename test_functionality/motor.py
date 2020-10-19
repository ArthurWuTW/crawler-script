import RPi.GPIO as GPIO
import time
 
In1, In2 = 6, 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)
 
try:
    while True:
        print('on')
        GPIO.output(In1, GPIO.HIGH)
        GPIO.output(In2, GPIO.LOW)
        time.sleep(5)
        print('reverse')
        GPIO.output(In2, GPIO.HIGH)
        GPIO.output(In1, GPIO.LOW)
        time.sleep(5)
        break
except KeyboardInterrupt:
    print('aaa')
finally:
    GPIO.cleanup()
