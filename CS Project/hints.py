
def flagFinder(app,isAi):
    if app.numClicks ==0:
        print("no information")
    else:
        found = False
        for row in range(len(app.board)):
            
            for col in range(len(app.board[0])):
                if app.board[row][col].number==0 or (not app.board[row][col].clicked) :
                    continue
                if len(mines(app,row,col)) == app.board[row][col].number:
                    mine = mines(app,row,col)
                    while len(mine)>0 and app.board[mine[0][0]][mine[0][1]].hasFlag:
                        mine = mine[1:]
                    if len(mine)==0:
                        continue
                    app.board[mine[0][0]][mine[0][1]].color = "red"
                    found = True
                    break
            if found:
                break
                    
        if not found and not isAi:
            app.message = "make a move to uncover more information for your hint"
        elif found:
            return mine[0]
        else:
            return None
                    
def mines(app,row,col):
    possible = []
    for rows in range(max(0,row-1),min(row+2,len(app.board))):
        for cols in range(max(0,col-1), min(col+2, len(app.board[0]))):
            if (not app.board[rows][cols].clicked) :
                possible.append([rows,cols])
    return possible
