#!/usr/bin/python

import RPi.GPIO as GPIO
from pygame import mixer
import time

# globals
LED_PIN = 2 #I2C SDA 
MOTION_SENSOR_PIN = 14 # UART TX

def GpioConfig():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
    GPIO.output(LED_PIN, GPIO.LOW)


def MixerConfig():
    mixer.init()
    return mixer.Sound('witchlaf2.wav')

# MAIN

GpioConfig()
sound = MixerConfig()

startTime = time.time()

try:
    while True:
        
        timeNow = time.time()
        if GPIO.input(MOTION_SENSOR_PIN) and (timeNow - startTime >= 4.0):
            print('Motion Detected!')
            sound.play()

            startTime = timeNow

except KeyboardInterrupt:
    pass


mixer.quit()
GPIO.cleanup()


