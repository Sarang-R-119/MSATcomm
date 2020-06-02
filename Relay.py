import RPi.GPIO as GPIO
import time


def setupRelay():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(12,GPIO.OUT)

def relaySwitchON():
	    print("Relay ON")
	    GPIO.output(12,GPIO.LOW)

def relaySwitchOFF():
	    print("Relay OFF")
	    GPIO.output(12,GPIO.HIGH)