#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time
import subprocess

subprocess.call(['./setup.sh'])

def alert(channel):
    
    time.sleep(0.25)
    
    print('It\'s hot in here')
    if(channel == 'P9_41'):
        temp1 = bus.read_byte_data(address1, 0)
        temp1F = (temp1 * (9/5)) + 32
        print ('Temp1: ' + str(temp1F))
        
    elif(channel == 'P9_42'):
        temp2 = bus.read_byte_data(address2, 0)
        temp2F = (temp2 * (9/5)) + 32
        print ('Temp2: ' + str(temp2F))
        
    time.sleep(0.25)
        
    
alert1 = 'P9_41'
alert2 = 'P9_42'
    
GPIO.setup(alert1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(alert2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
GPIO.add_event_detect(alert1, GPIO.BOTH, callback=alert)
GPIO.add_event_detect(alert2, GPIO.BOTH, callback=alert)
    
bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x49
    
bus.write_byte_data(address1, 3, 0x1C) 
bus.write_byte_data(address1, 2, 0x1B) 
bus.write_byte_data(address1, 1, 0x84)
bus.write_byte_data(address2, 3, 0x1C) 
bus.write_byte_data(address2, 2, 0x1B) 
bus.write_byte_data(address2, 1, 0x84)

while True:
    pass