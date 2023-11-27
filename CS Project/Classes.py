import copy
from cmu_graphics import *

class cell():
    def __init__(self):
        self.hasFlower = False
        self.number = None
        self.clicked = False
        self.safe = False
        self.trueFlag = False
        self.hasFlag = False
        self.extraLifes = 0
        self.color = 'purple'
    def __repr__(self):
        return f"{self.hasFlower},{self.number},{self.clicked}"
    def setFlower(self,flower):
        self.hasFlower = flower
    def makeSafe(self):
        self.safe = True
    def isSafe(self):
        return self.safe
    def addNumber(self,number):
        self.number= number
    def clickSquare(self):
        self.clicked = True
        self.color = 'beige'
    def checkFlower(self):
        return self.hasFlower
    def flag(self,app,isAi):
        if not self.hasFlag:
            if app.flagCount>0:
                self.color = 'green'
                app.flagCount-=1
                self.hasFlag = True
            elif isAi:
                app.message = "you have incorrect flags"

        else:
            self.hasFlag = False
            app.flagCount+=1
            self.color = 'purple'
        
        
    def drawCell(self,left,top,width,height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        drawRect(left,top,width,height,border = 'white',fill = self.color)
        if self.clicked:
            if not (self.number==0):
                drawLabel(f"{self.number}",left+width//2,top+height//2)
        elif self.hasFlag:
            drawLabel("flag",left+width//2,top+height//2)
        
    def inCell(self,x,y):
        return (self.left<x<self.left+self.width) and (self.top<y<self.top+self.height)
class button():
    def __init__(self,label):
        self.label = label
    def drawButton(self,left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        drawRect(left,top,width,height,fill = 'orange',border = 'black')
        drawLabel(self.label, left+width//2,top+height//2)
    def inButton(self,x,y):
        return (self.left<x<self.left+self.width) and (self.top<y<self.top+self.height)
