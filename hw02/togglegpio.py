#!/usr/bin/env python3
"""
Isaac Lau
ECE 434- hw02: Toggles the GPIO at MAX SPEED
"""

import Adafruit_BBIO.GPIO as GPIO
import time


L1 = "P9_15"

GPIO.setup(L1, GPIO.OUT)

try:
    while True:
        GPIO.output(L1, GPIO.HIGH)
        GPIO.output(L1, GPIO.LOW)
            
except KeyboardInterrupt:
    GPIO.cleanup()