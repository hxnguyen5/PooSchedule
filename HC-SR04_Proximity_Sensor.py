# This program utilizes the HC-SR04 proximity sensor
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
# Set up Trigger Pin
TRIG = 16
# Set up Echo Pin
# Do not forget the Voltage Divider
# R1 is 1K and R2 is 2K
ECHO = 18

print "Distance Measurement in Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

# Ensure Trigger Pin is set to low and give sensor time to settle

GPIO.output(TRIG,False)
print "Waiting for Sensor to Settle"
time.sleep(2)

# Trigger a 10 microseconds pulse

GPIO.output(TRIG,True)
time.sleep(0.00001)
GPIO.output(TRIG,False)

# Mark time just before return signal is received

while GPIO.input(ECHO)==0:
	pulse_start = time.time()
while GPIO.input(ECHO)==1:
	pulse_end = time.time()

# Calculate time delta

pulse_duration = pulse_end - pulse_start

# Calculate Distance; note that we use 343 m/s for the speed of sound
# Also converted to cm/s

distance = pulse_duration*17150

distance = round(distance,2)

print ("Distance", distance, "cm")

GPIO.cleanup()
