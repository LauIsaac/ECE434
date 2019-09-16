#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
import time

clear = 'P9_11'
left  = 'P9_13' 
down  = 'P9_17'
up    = 'P9_27'
right = 'P8_17'


def printHelper(grid):
    for row in grid:
        for e in row:
            print(e, end = " ")
        print()

def updateBoard(channel):
    global playerX
    global playerY
    global board
    
    board[playerY][playerX] = 'X'
    
    if channel == up:
        playerY -= 1
    elif channel == down:
        playerY += 1
    elif channel == left:
        playerX -= 1
    elif channel == right:
        playerX += 1
    elif channel == clear:
        clearBoard()
        
    board[playerY][playerX] = 'P'
    printHelper(board)
    
def clearBoard():
    global board
    global playerX
    global playerY
    n = 15
    m = 11
    board = [['-'] * m for i in range(n)]
    
    board[playerY][playerX]
    
    
    
def main():
    
    global playerX
    global playerY
    global board
    
    GPIO.setup(left,  GPIO.IN)
    GPIO.setup(down,  GPIO.IN)
    GPIO.setup(up,    GPIO.IN)
    GPIO.setup(right, GPIO.IN)
    GPIO.setup(clear, GPIO.IN)
    
    GPIO.add_event_detect(up,   GPIO.BOTH, callback=updateBoard, bouncetime=500)
    GPIO.add_event_detect(down, GPIO.BOTH, callback=updateBoard, bouncetime=500)
    GPIO.add_event_detect(left, GPIO.BOTH, callback=updateBoard, bouncetime=500)
    GPIO.add_event_detect(right,GPIO.BOTH, callback=updateBoard, bouncetime=500)
    GPIO.add_event_detect(clear,GPIO.BOTH, callback=updateBoard, bouncetime=500)
    
    board[playerY][playerX] = 'P'
    
    printHelper(board)
        
    try:
        
        while True:
            time.sleep(100)
            
    except KeyboardInterrupt:
        print("Cleaning Up")
        GPIO.cleanup()
        

if __name__ == "__main__":
    """ This is executed when run from the command line """
     #This is the size of the board and the init player location
    n = 11
    m = 11
    playerX = 6
    playerY = 6
    
     #This initialized the board to null and then adds the player's location
    board = [['-'] * m for i in range(n)]
    
    main()