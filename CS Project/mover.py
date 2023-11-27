
from hints import *
from board import *
def move(app,board):
    if app.numClicks ==0:
        board = makeFirstMove(app,board)
        
    #elif falseFlags():
    # remove false flags
    elif flagFinder(app,True)!=None: # has guaranteed Mines
        board =placeFlags(app,board)
    else:
        for row in range(len(board)):
            for col in range(len(board[0])):
                elem = board[row][col]
                if (not elem.clicked) or (elem.number ==0):
                    continue
                if len(safeClicks(app,board,row,col,elem.number))>0 :
                    possible = safeClicks(app,board, row,col,elem.number)
                    print(possible)
                    click = [possible[0]]
                    clickBoard(app,board,click)
                else:
                    pass
                    #hardSolve(app,board)
    return board
def safeClicks(app,board,row,col,num):
    store = []
    for rows in range(max(0,row-1),min(row+2,len(board))):
        for cols in range(max(0,col-1),min(col+2,len(board[0]))):
            if board[rows][cols].trueFlag:
                num-=1
            elif not board[rows][cols].clicked:
                store.append([rows,cols])
    if num==0:
        return store
    else:
        return []
def hardSolve(app,board):
    if isSolved(board):
        return move
def isSolved(board):
    for row in board:
        for elem in row:
            if not (elem.hasFlower or elem.clicked):
                return False
    return True
def makeFirstMove(app,board):
    app.drawMario = True
    app.mX,app.mY = app.boardLeft+app.boardWidth//2, app.boardTop + app.boardHeight//2
    board = writeNumbers(placeMines(board,(app.size//8)*13,app.size//2,app.size//2))
    app.numClicks+=1
    clickBoard(app,board,[[app.size//2,app.size//2]])
    return board
def placeFlags(app,board):
    flag1 = flagFinder(app,True)
    board[flag1[0]][flag1[1]].flag(app,True)
    board[flag1[0]][flag1[1]].trueFlag = True
    return board