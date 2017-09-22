import time
import RPi.GPIO as GPIO
from subprocess import check_output

#GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(29, GPIO.OUT) #G  
GPIO.setup(31, GPIO.OUT) #F
GPIO.setup(33, GPIO.OUT)#A
GPIO.setup(35, GPIO.OUT)#B
GPIO.setup(37, GPIO.OUT)#E
GPIO.setup(32, GPIO.OUT)#D
GPIO.setup(36, GPIO.OUT)#C
GPIO.setup(38, GPIO.OUT)#P

#Numbers 0-9

def Zero():
    GPIO.output(29, False)#G
    GPIO.output(31, True)#F
    GPIO.output(33, True)#A
    GPIO.output(35, True)#B
    GPIO.output(37, True)#E
    GPIO.output(32, True)#D
    GPIO.output(36, True)#C
    GPIO.output(38, True)#P
    

def One():
    GPIO.output(29, False)#G
    GPIO.output(31, False)#F
    GPIO.output(33, False)#A
    GPIO.output(35, True)#B
    GPIO.output(37, False)#E
    GPIO.output(32, False)#D
    GPIO.output(36, True)#C
    GPIO.output(38, True)#P
def Two():
    GPIO.output(29, True)#G
    GPIO.output(31, False)#F
    GPIO.output(33, True)#A
    GPIO.output(35, True)#B
    GPIO.output(37, True)#E
    GPIO.output(32, True)#D
    GPIO.output(36, False)#C
    GPIO.output(38, True)#P
def Three():
    GPIO.output(29, True)#G
    GPIO.output(31, False)#F
    GPIO.output(33, True)#A
    GPIO.output(35, True)#B
    GPIO.output(37, False)#E
    GPIO.output(32, True)#D
    GPIO.output(36, True)#C
    GPIO.output(38, True)#P
def Four():
    GPIO.output(29, True)#G
    GPIO.output(31, True)#F
    GPIO.output(33, False)#A
    GPIO.output(35, True)#B
    GPIO.output(37, False)#E
    GPIO.output(32, False)#D
    GPIO.output(36, True)#C
    GPIO.output(38, False)#P
def Five():
    GPIO.output(29, True)#G
    GPIO.output(31, True)#F
    GPIO.output(33, True)#A
    GPIO.output(35, False)#B
    GPIO.output(37, False)#E
    GPIO.output(32, True)#D
    GPIO.output(36, True)#C
    GPIO.output(38, False)#P
def Six():
    GPIO.output(29, True)#G
    GPIO.output(31, True)#F
    GPIO.output(33, True)#A
    GPIO.output(35, False)#B
    GPIO.output(37, True)#E
    GPIO.output(32, True)#D
    GPIO.output(36, True)#C
    GPIO.output(38, True)#P
def Seven():
    GPIO.output(29, False)#G
    GPIO.output(31, False)#F
    GPIO.output(33, True)#A
    GPIO.output(35, True)#B
    GPIO.output(37, False)#E
    GPIO.output(32, False)#D
    GPIO.output(36, True)#C
    GPIO.output(38, False)#P
def Eight():
    GPIO.output(29, True)#G
    GPIO.output(31, True)#F
    GPIO.output(33, True)#A
    GPIO.output(35, True)#B
    GPIO.output(37, True)#E
    GPIO.output(32, True)#D
    GPIO.output(36, True)#C
    GPIO.output(38, True)#P
def Nine():
    GPIO.output(29, True)#G
    GPIO.output(31, True)#F
    GPIO.output(33, True)#A
    GPIO.output(35, True)#B
    GPIO.output(37, False)#E
    GPIO.output(32, True)#D
    GPIO.output(36, True)#C
    GPIO.output(38, True)#P
    
#Stop when finished
def Stop():
    GPIO.output(29, False)#G
    GPIO.output(31, False)#F
    GPIO.output(33, False)#A
    GPIO.output(35, False)#B
    GPIO.output(37, False)#E
    GPIO.output(32, False)#D
    GPIO.output(36, False)#C
    GPIO.output(38, False)#P    


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
        speak = check_output(['espeak', 'Come on man you are killing me'])
        time.sleep(0.65)
        print("Type a number from 0-9")
    elif KeyPress == "7":
        print("7 is showing")
        Seven()
        time.sleep(0.65)
        speak = check_output(['espeak', 'I hope you have a huge toilet at home'])
        time.sleep(0.65)
        print("Type a number from 0-9")
    elif KeyPress == "8":
        print("8 is showing")
        Eight()
        time.sleep(0.65)
        speak = check_output(['espeak', 'Hey What are you waiting for'])
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
    
    
   
