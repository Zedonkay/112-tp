from cmu_graphics import *
import os, pathlib, PIL.Image, random, math, string
from board import *
from hints import *
from Classes import *
from mover import *
def onAppStart(app):
    app.mario = CMUImage(PIL.Image.open("images/mario.png"))
    app.drawMario = False
    app.width = 1600
    app.height = 1100
    app.mX = 40
    app.mY = 40
    app.size = None
    app.boardLeft = 450
    app.time = 0
    app.boardWidth = 700
    app.boardTop =300
    app.boardHeight = 700
    app.openingScreen = True
    app.game = False
    app.flagCount = 0
    runScreen(app)
    app.board = None
    app.loss = False
    app.numClicks = 0
    app.win = False
    app.stepsPerSecond = 4
    app.displayTime = 0
    app.message = None
def onStep(app):
    if app.message !=None:
        app.displayTime+=1
    if app.displayTime==12:
        app.message = None
        app.displayTime = 0
    if app.numClicks!=0:
        app.time+=1
    if app.size !=None:
        app.game = True
    if app.game:
        if isSolved(app.board):
            app.game = False
            app.win = True
    else:
        
        app.drawMario = False
def onKeyPress(app,key):
    if key == 'r':
        main()
    elif key == 'f' and app.game:
        flagFinder(app,False)
    elif key == 'm' and app.game:
        app.board = move(app,app.board)
def onMousePress(app,mouseX,mouseY, button):
    if app.openingScreen:
        if app.medium.inButton(mouseX,mouseY) and button == 0:
            app.openingScreen = False
            app.size = 8
            app.flagCount = 13
            runBoard(app)
           
        elif app.hard.inButton(mouseX,mouseY) and button == 0:
            app.openingScreen = False
            app.size = 16
            app.flagCount = 26
            runBoard(app)
            
    if app.game:
        for row in range(len(app.board)):
            for col in range(len(app.board[0])):
                if app.board[row][col].inCell(mouseX,mouseY) and button ==0:
                    if app.numClicks ==0:
                        app.drawMario = True
                        app.mX,app.mY = mouseX,mouseY
                        app.board = writeNumbers(placeMines(app.board,(app.size//8)*13,row,col))
                        app.numClicks+=1
                    clickBoard(app,app.board,[[row,col]])
                elif app.board[row][col].inCell(mouseX,mouseY) and button ==2 and not (app.numClicks ==0) and not app.board[row][col].clicked:
                    app.board[row][col].flag(app,False)
def onMouseMove(app, mouseX,mouseY):
    if app.numClicks!=0 and app.game:
        for row in app.board:
            for elem in row:
                if elem.inCell(mouseX,mouseY) and elem.clicked:
                    app.mX,app.mY = mouseX, mouseY
def getWidthHeight(app):
    return ((app.boardWidth//app.size),(app.boardHeight//app.size))

def getCellTopLeft(app,row,col):  
    pass
def redrawAll(app):
    if app.loss:
        drawGameOver(app)
        
    elif app.openingScreen:
        drawScreen(app)
        
    elif app.game:
        drawLabel(f"Time: {app.time//4}",app.width//2,50,size = 30)
        drawLabel(f"Flags Left: {app.flagCount}",app.width//2, 100, size = 30)
        drawLabel("click f for a guaranteed flag location",app.width//2,150,size = 30)
        if app.displayTime!=0 :
            drawLabel(app.message, app.width//2,200,size  =30)
        width,height = getWidthHeight(app)
        for row in range(app.size):
            for col in range(app.size):
                app.board[row][col].drawCell(app.boardLeft+(width*col),app.boardTop+height*row,width,height)
    elif app.win:
        drawLabel(f"you won in {app.time//4} seconds",app.width//2,200,size = 50)
    if app.drawMario:
        drawMario(app)
        
        
def drawGameOver(app):
    drawLabel("gameover",200,200,size=50)            
def runScreen(app):
    app.medium = button("medium")
    app.hard = button("hard")
def drawScreen(app):
    app.medium.drawButton(50,50,200,100)
    app.hard.drawButton(50,250,200,100)
def runBoard(app):
    app.board = initializeBoard(app.size)
def drawMario(app):
    
    drawImage(app.mario,app.mX,app.mY,width = 30,height = 60)

def main():
    runApp()

main()