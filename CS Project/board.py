import random
import copy 
from Classes import *
def prettyPrint(board):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))
def initializeBoard(size):
    return [[cell() for i in range(size)]  for j in range(size)]
def placeMines(board,mines,clickedRow,clickedCol):
    for row in range(max(0,clickedRow-2),min(len(board),clickedRow+3)):
        for col in range(max(0,clickedCol-2),min(len(board[0]),clickedCol+3)):
            board[row][col].makeSafe()
    size = len(board)**2
    while(mines>0):
        for rows in range(0,len(board)):
            
            for cols in range(0,len(board[0])):
                if board[rows][cols].isSafe():
                    continue

                if mines == 0:
                    break
                if board[rows][cols].checkFlower():
                    continue
                prob = findProbability(board,rows,cols,(mines/size) )
                board[rows][cols].setFlower(random()<prob)
                if board[rows][cols].checkFlower():
                    mines-=1
                    
            if mines ==0:
                break
    return board

def findProbability(board,row,col,base):
    for rows in range(0,len(board)):
        for cols in range(0,len(board[0])):
            if board[rows][cols].hasFlower:
                base-= (((10/64)/8)/( ((rows-row)**2+(cols-col)**2 )**0.25   ))*0.4
                
    if base<=0:
        
        return 0.01
    return base
def writeNumbers(board):
    for rows in range(len(board)):
        for cols in range(len(board[0])):
            if not board[rows][cols].checkFlower():
                board[rows][cols].addNumber(findNumber(board,rows,cols))
            else:
                board[rows][cols].addNumber("A")
    return board
def findNumber(board,row,col):
    num = 0
    for rows in range(max(0,row-1),min(len(board),row+2)):
        for cols in range(max(0,col-1),min(len(board[0]),col+2)):
            if board[rows][cols].checkFlower() and not (rows == row  and cols==col) :
                num+=1
   
    return num

def clickBoard(app,board,check):
    
    while len(check)>0: 
        firstCheck = check[0]
        check = check[1:]
        if not board[firstCheck[0]][firstCheck[1]].hasFlag:
            if board[firstCheck[0]][firstCheck[1]].checkFlower():
                app.loss = True
                app.game = False
                return
            if board[firstCheck[0]][firstCheck[1]].number ==0:
                for row in range(max(0,firstCheck[0]-1),min(len(board),firstCheck[0]+2)):
                    for col in range(max(0,firstCheck[1]-1),min(len(board[0]),firstCheck[1]+2)):
                        if board[row][col].number ==0 and not board[row][col].clicked:
                            check.append([row,col])
                        board[row][col].clickSquare()
            else:
                board[firstCheck[0]][firstCheck[1]].clickSquare()
        
    return board