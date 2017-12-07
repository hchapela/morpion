#-----------------------------------------------------

def initGrid(n,val):
    grid=[]
    for j in range(n):
        x=[val]*n
        grid=grid+[x]
    return grid

#-----------------------------------------------------

def printGrid(grid):
    for j in grid:
        for el in j:
            print(el,"\t", end='')
        print()

#-----------------------------------------------------

def assignGrid(pion,grid):
    x=4
    y=4
    cond=True
    while(cond==True):
        x=int(input("Entrez colonne"))-1
        y=int(input("Entrez ligne"))-1
        if  x>=0 and x<3 and y>=0 and x<3:
            if grid[y][x]==".":
                grid[y][x]=pion
                cond=False
                return grid
            else:
                return False

#-----------------------------------------------------

def egalite(gr):
    for i in gr:
        for el in i:
            if el==".":
                 return False
    return True

#-----------------------------------------------------

def checkWin(grid, char):
    x = 0
    y = 0
    state = False
    #TEST BY COLUMN
    while(x < 3):
        while(y < 3 and grid[y][x] == char):
            y += 1
            if(y == 3):
                state = True
        y = 0
        x += 1
    #TEST BY LINE
    while(y < 3):
        while(x < 3 and grid[y][x] == char):
            x += 1
            if(x == 3):
                state = True
        x = 0
        y += 1
    #TEST CROSS
    if(grid[0][0] == char and grid[1][1] == char and grid[2][2] == char):
        state = True
    if(grid[0][2] == char and grid[1][1] == char and grid[2][0] == char):
        state = True
    return state

#-----------------------------------------------------

def main():
    row = 0
    grid = initGrid(3, ".")
    partie = False
    while(partie == False) and (checkWin(grid, "X") == False) and (checkWin(grid, "O") == False):
        if row % 2 == 0:
            char = "X"
        else:
            char = "O"
        state = assignGrid(char, grid)
        if state != False:
            row += 1
            printGrid(state)
        partie = egalite(grid)
    print("END OF THE GAME PLAYER :", char, " WON THE GAME")

#-----------------------------------------------------

main()
