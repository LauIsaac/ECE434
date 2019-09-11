#!/usr/bin/env python3
"""
ECE434 HW1 Part 6: Etch-a-sketch

A simple etch-a-sketch program 
"""

__author__ = "Isaac Lau"
__version__ = "0.1.0"
__license__ = "MIT"


def printHelper(grid):
    for row in grid:
        for e in row:
            print(e, end = " ")
        print()
    

def main():
    """ Main entry point of the app """
    n = 15
    m = 15
    playerX = 7 
    playerY = 7
    board = [["-"] * m for i in range(n)]
    board[playerY][playerX] = 'P'
    
    printHelper(board)
    
    while True:
        
        board[playerY][playerX] = 'X'
        
        command = input('Please enter a direction (up, down, left, right, clear): ')
        if command == 'up':
            playerY -= 1
            
        elif command == 'down':
            playerY += 1
            
        elif command == 'left':
            playerX -= 1
            
        elif command == 'right':
            playerX += 1
            
        elif command == 'clear':
            board = [["-"] * m for i in range(n)]

        board[playerY][playerX] = 'P'
        
        printHelper(board)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()