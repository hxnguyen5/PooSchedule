# This file use keyboard inputs to control two motors via an L298N H-Bridge.
# Four input pins are setup for two motors; two for reverse direction and 
# two for forward direction.

import time
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# Main Program
GPIO.output(11, True)
time.sleep(1)
GPIO.output(11, False)
GPIO.output(13, True)
time.sleep(1)
GPIO.output(13, False)
GPIO.output(7, True)
time.sleep(1)
GPIO.output(7, False)
GPIO.output(15, True)
time.sleep(1)
GPIO.output(15, False)
GPIO.cleanup()
