def printTab(tab):
    for i in tab:
        print(i)

def assignTab(tab):
    x = -1
    y = -1
    while(x < 0 or x > 2):
        x = input("posX : ")
    while(y < 0 or y > 2):
        y = input("posY : ")
    tab[x][y] = "X"
    return tab

def checkTab(tab):
    x = 0
    y = 0
    for i in range(tab):
        for j in range(tab):

def main():
    tab = [".", ".", "."]
    tab[0] = [".", ".", "."]
    tab[1] = [".", ".", "."]
    tab[2] = [".", ".", "."]
    while(checkTab(tab) == True):
        tab = assignTab(tab)
        printTab(tab)


main()
