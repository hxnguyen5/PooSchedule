import time
import RPi.GPIO as GPIO
from espeak import espeak
from datetime import datetime
from subprocess import check_output

#GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT) #G  
GPIO.setup(6, GPIO.OUT) #F
GPIO.setup(13, GPIO.OUT)#A
GPIO.setup(19, GPIO.OUT)#B
GPIO.setup(26, GPIO.OUT)#E
GPIO.setup(16, GPIO.OUT)#D
GPIO.setup(20, GPIO.OUT)#C
GPIO.setup(21, GPIO.OUT)#P

#Numbers 0-9

def Zero():
    GPIO.output(5, False)#G
    GPIO.output(6, True)#F
    GPIO.output(13, True)#A
    GPIO.output(19, True)#B
    GPIO.output(26, True)#E
    GPIO.output(16, True)#D
    GPIO.output(20, True)#C
    GPIO.output(21, True)#P
    

def One():
    GPIO.output(5, False)#G
    GPIO.output(6, False)#F
    GPIO.output(13, False)#A
    GPIO.output(19, True)#B
    GPIO.output(26, False)#E
    GPIO.output(16, False)#D
    GPIO.output(20, True)#C
    GPIO.output(21, True)#P
def Two():
    GPIO.output(5, True)#G
    GPIO.output(6, False)#F
    GPIO.output(13, True)#A
    GPIO.output(19, True)#B
    GPIO.output(26, True)#E
    GPIO.output(16, True)#D
    GPIO.output(20, False)#C
    GPIO.output(21, True)#P
def Three():
    GPIO.output(5, True)#G
    GPIO.output(6, False)#F
    GPIO.output(13, True)#A
    GPIO.output(19, True)#B
    GPIO.output(26, False)#E
    GPIO.output(16, True)#D
    GPIO.output(20, True)#C
    GPIO.output(21, True)#P
def Four():
    GPIO.output(5, True)#G
    GPIO.output(6, True)#F
    GPIO.output(13, False)#A
    GPIO.output(19, True)#B
    GPIO.output(26, False)#E
    GPIO.output(16, False)#D
    GPIO.output(20, True)#C
    GPIO.output(21, False)#P
def Five():
    GPIO.output(5, True)#G
    GPIO.output(6, True)#F
    GPIO.output(13, True)#A
    GPIO.output(19, False)#B
    GPIO.output(26, False)#E
    GPIO.output(16, True)#D
    GPIO.output(20, True)#C
    GPIO.output(21, False)#P
def Six():
    GPIO.output(5, True)#G
    GPIO.output(6, True)#F
    GPIO.output(13, True)#A
    GPIO.output(19, False)#B
    GPIO.output(26, True)#E
    GPIO.output(16, True)#D
    GPIO.output(20, True)#C
    GPIO.output(21, True)#P
def Seven():
    GPIO.output(5, False)#G
    GPIO.output(6, False)#F
    GPIO.output(13, True)#A
    GPIO.output(19, True)#B
    GPIO.output(26, False)#E
    GPIO.output(16, False)#D
    GPIO.output(20, True)#C
    GPIO.output(21, False)#P
def Eight():
    GPIO.output(5, True)#G
    GPIO.output(6, True)#F
    GPIO.output(13, True)#A
    GPIO.output(19, True)#B
    GPIO.output(26, True)#E
    GPIO.output(16, True)#D
    GPIO.output(20, True)#C
    GPIO.output(21, True)#P
def Nine():
    GPIO.output(5, True)#G
    GPIO.output(6, True)#F
    GPIO.output(13, True)#A
    GPIO.output(19, True)#B
    GPIO.output(26, False)#E
    GPIO.output(16, True)#D
    GPIO.output(20, True)#C
    GPIO.output(21, True)#P
    
#Stop when finished
def Stop():
    GPIO.output(5, False)#G
    GPIO.output(6, False)#F
    GPIO.output(13, False)#A
    GPIO.output(19, False)#B
    GPIO.output(26, False)#E
    GPIO.output(16, False)#D
    GPIO.output(20, False)#C
    GPIO.output(21, False)#P    


print("Type a number from 0-9")
while True:    
    
    KeyPress = input()
    
    if KeyPress == "0":
        print("0 is showing")
        Zero()
        time.sleep(0.65)
        print("Type a number from 0-9")
    elif KeyPress == "1":
        print("1 is showing")
        One()
        time.sleep(0.65)
        print("Type a number from 0-9")
    elif KeyPress =="2":
        print("2 is showing")
        Two()
        time.sleep(0.65)
        speak = check_output(['espeak', 'Hey you need to go poopoo it has been two days already'])
        time.sleep(0.65)
        print("Type a number from 0-9")
    elif KeyPress == "3":
        print("3 is showing")
        Three()
        time.sleep(0.65)
        speak = check_output(['espeak', 'Hey you need to go poopoo it stinks in here'])
        time.sleep(0.65)
        print("Type a number from 0-9")
    elif KeyPress == "4":
        print("4 is showing")
        Four()
        time.sleep(0.65)
        speak = check_output(['espeak', 'Hey you need to go poopoo your stomach is getting big'])
        time.sleep(0.65)
        print("Type a number from 0-9")
    elif KeyPress == "5":
        print("5 is showing")
        Five()
        time.sleep(0.65)
        speak = check_output(['espeak', 'Hey you need to go poopoo before your belly blows up'])
        time.sleep(0.65)
        print("Type a number from 0-9")
    elif KeyPress == "6":
        print("6 is showing")
        Six()
        time.sleep(0.65)
        speak = check_output(['espeak', 'Hey you need to go poopoo come on man you are killing me'])
        time.sleep(0.65)
        print("Type a number from 0-9")
    elif KeyPress == "7":
        print("7 is showing")
        Seven()
        time.sleep(0.65)
        speak = check_output(['espeak', 'Hey you need to go poopoo i hope you have a huge toilet at home'])
        time.sleep(0.65)
        print("Type a number from 0-9")
    elif KeyPress == "8":
        print("8 is showing")
        Eight()
        time.sleep(0.65)
        speak = check_output(['espeak', 'Hey you need to go poopoo what are you waiting for'])
        time.sleep(0.65)
        speak = check_output(['espeak', 'Someone to pull your pants down for you'])
        time.sleep(0.65)
        print("Type a number from 0-9")
    elif KeyPress == "9":
        print("9 is showing")
        Nine()
        time.sleep(0.65)
        speak = check_output(['espeak', 'Hey I am serious man go poo already'])
        time.sleep(0.65)
        print("Type a number from 0-9")
    else:
        Stop()
        print("Type a number from 0-9")
    
    
   
