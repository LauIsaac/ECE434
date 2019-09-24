#!/usr/bin/python3

from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
import time
import smbus
from subprocess import call

def eraseBoard():
    
    global red
    global green
    global board
    
    board = [ [0] * 8 for _ in range(8)]
    
    writeDisplay()
    

def writeDisplay():
    
    global verticalMatrix
    global green
    global red
    
    horizontalMatrix = [0x00,0x02,0x04,0x06,0x08,0x0A,0x0C,0x0E]
    
    green = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]

    for i in range(8):
        for j in range(8):
            green[i] += board[i][j] * verticalMatrix[j]
            
    for i in range(8):
        bus.write_i2c_block_data(matrix,horizontalMatrix[i],[green[i],red[i]])
        

def clamp(N, minN, maxN):
    return max(min(maxN,N), minN)

    
def main():
    
    global userX
    global userY
    global board
    
    global encoder1
    global encoder2
    
    try:
        while True:
            time.sleep(0.5)
            global horizontalPos
            global verticalPos
            global red
            global green
            global verticalMatrix
            
            oldUserX = userX
            oldUserY = userY
            
            temp=bus.read_byte_data(address,0)
            
            if(temp>=26):
                eraseBoard()
                
                
            if(encoder1.position < horizontalPos):
                userX += 1
                
            elif(encoder1.position > horizontalPos):
                userX -= 1
            
            elif(encoder2.position < verticalPos):
                userY += 1
                
            elif(encoder2.position > verticalPos):
                userY -= 1
                
            
            horizontalPos = encoder1.position
            verticalPos = encoder2.position
            
            userX = clamp(userX,0,7)
            userY = clamp(userY,0,7)
            
            
            red[oldUserX] = red[oldUserX] - verticalMatrix[oldUserY]
            red[userX]    = red[userX] + verticalMatrix[userY]
            
            if(oldUserX != userX or oldUserY != userY):
                board[userX][userY] = 1
                
            
            writeDisplay()
            
    
    except KeyboardInterrupt:
        print(' Thanks for playing!')
        
        
    
if __name__ == "__main__":
    """ This is executed when run from the command line """
     #Initialise the user's location on the board
     
    userX = 4
    userY = 4
     
    verticalPos = 0
    horizontalPos = 0
     
    bus = smbus.SMBus(2)    # Use i2c bus 1
    matrix = 0x70           # Use address 0x70 for display
    address = 0x48          # Use address 0x48 for temp sensor
    
    bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
    bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
    bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)
    
    greenBoard = [ [0] * 8 for _ in range(8) ]
    
    verticalMatrix = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]
    
    green = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    red   = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    
    eraseBoard()
    
    
    encoder1 = RotaryEncoder(eQEP1)
    encoder2 = RotaryEncoder(eQEP2)
    
    encoder1.setAbsolute()
    encoder2.setAbsolute()
    encoder1.enable()
    encoder2.enable()
    
    red[userX] = red[userX] + verticalMatrix[userY]
    
    main()

        

            
            
            
            


