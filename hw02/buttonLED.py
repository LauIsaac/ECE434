#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
import time

buttonClear = 'P9_11'
buttonLeft  = 'P9_13' 
buttonDown  = 'P9_17'
buttonUp    = 'P9_27'
buttonRight = 'P8_17'

LEDleft     = 'P8_7'
LEDup       = 'P8_9'
LEDdown     = 'P8_11'
LEDright    = 'P8_13'


map = {buttonLeft: LEDleft, buttonUp: LEDup, buttonDown: LEDdown, buttonRight: LEDright} #

GPIO.setup(LEDleft,     GPIO.OUT)
GPIO.setup(LEDup,       GPIO.OUT)
GPIO.setup(LEDdown,     GPIO.OUT)
GPIO.setup(LEDright,    GPIO.OUT)

GPIO.setup(buttonLeft,  GPIO.IN)
GPIO.setup(buttonDown,  GPIO.IN)
GPIO.setup(buttonUp,    GPIO.IN)
GPIO.setup(buttonRight, GPIO.IN)

def updateLED(channel):
    state = GPIO.input(channel)
    GPIO.output(map[channel], state)
    
    
GPIO.add_event_detect(buttonRight,  GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(buttonLeft,   GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(buttonUp,     GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(buttonDown,   GPIO.BOTH, callback=updateLED)
    
try:
    
    while True:
        time.sleep(100)
        
except KeyboardInterrupt:
    print("\nCleaning Up")
    GPIO.cleanup()