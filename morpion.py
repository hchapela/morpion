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

def assignGrid(grid, char):
    x = 4
    y = 4
    print("")
    while(x < 0 or x >= 3):
        x = int(input("x = ")) - 1
    while(y < 0 or y >= 3):
        y = int(input("y = ")) - 1
    grid[y][x] = char
    return grid

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
    while(checkWin(grid, "X") == False and checkWin(grid, "O") == False):
        if row % 2 == 0:
            char = "X"
        else:
            char = "O"
        grid = assignGrid(grid, char)
        print("\n","row : ", row, "***************************************", "\n")
        printGrid(grid)
        row += 1
    print("END OF THE GAME PLAYER :", char, " WON THE GAME")

#-----------------------------------------------------

main()
