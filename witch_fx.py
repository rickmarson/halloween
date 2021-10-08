#!/usr/bin/python

import RPi.GPIO as GPIO
import time

# globals
LED_PIN = 2 #I2C SDA 
SWITCH_PIN = 15 #UART RX
MOTION_SENSOR_PIN = 14 # UART TX

def GpioConfig():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
    GPIO.output(LED_PIN, GPIO.LOW)

# MAIN

GpioConfig()

switchPressed = False

startTime = time.time()

try:
    while True:

        if GPIO.input(MOTION_SENSOR_PIN):
            pass

        if GPIO.input(SWITCH_PIN):
            switchPressed = True 
        else:
            if (switchPressed):
                pass

        switchPressed = False

        # monitor the light state continously so that the led state can be changes even if we toggle the light from other system (e.g. Alexa)
        timeNow = time.time()
        if(timeNow - startTime >= 1.0):
            ChangeLedState()
            startTime = time.time()

except KeyboardInterrupt:
    pass


GPIO.cleanup()


