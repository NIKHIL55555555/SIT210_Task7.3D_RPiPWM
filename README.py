# SIT210_Task7.3D_RPiPWM
from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
from tkinter import ttk
import time
import RPi.GPIO as GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

GPIO_TriggerPin = 23
GPIO_EchoPin = 24

GPIO.setup(18, GPIO.OUT)   

GPIO.setup(GPIO_TriggerPin, GPIO.OUT)
GPIO.setup(GPIO_EchoPin, GPIO.IN)

def Distance():

    GPIO.output(GPIO_TriggerPin, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_TriggerPin, False)
 
    StartTime = time.time()
    StopTime = time.time()
  
    while GPIO.input(GPIO_EchoPin) == 0:
        TimeAtStart = time.time()
 
    while GPIO.input(GPIO_EchoPin) == 1:
        TimeAtStop = time.time()
 
    TimeElapsed = StopTime - StartTime
    Distance = (TimeElapsed * 34000) / 2
 
    return int(Distance)

led = GPIO.PWM(18, 500)
led.start(0)

try:
    while True:
        myvar = Distance()
        print ("Measured Distance = " + str(myvar) + " cm")
        if myvar < 100:
                led.ChangeDutyCycle(100 - myvar)
        else:
            led.start(0)

        time.sleep(0.75)
 
except KeyboardInterrupt:
    GPIO.cleanup()

