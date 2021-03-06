# This program using half-step control to turn the 28BYJ-48 stepper 
# motor one revolution using the ULN2003 stepper motor controller
# This motor uses 5VDC input and has 32 steps per revolution
# It also has a gear reduction of 1/64 which puts the resolution at
# 32x64 = 2048 steps per revolution for full-step and ..
# 32x64x2 = 4096 steps per revolution for half-step setup.

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ControlPin = [13,11,7,15]

for pin in ControlPin:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin,0)

seq = [	[1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
	[1,0,0,1]]

for i in range(512):
	for halfstep in range(8):
		for pin in range(4):
			GPIO.output(ControlPin[pin], seq[halfstep] [pin])
		time.sleep(0.001)

GPIO.cleanup()
