import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
while True:
    print "Relay on"
    GPIO.output(12,GPIO.LOW)
    time.sleep(3)
    print "Relay off"
    GPIO.output(12,GPIO.HIGH)
    time.sleep(3)
    
