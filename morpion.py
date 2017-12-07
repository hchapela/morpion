def printTab(tab):
    i = 0
    j = 0
    while(i < 3 and j < 3):
        while j != 2:
            print(tab[i][j])
            j += 1
        print(tab[i][j])
        j = 0
        i += 1

def assignTab(tab, char):
    x = -1
    y = -1
    while(x < 0 or x > 2):
        x = input("posX : ")
    while(y < 0 or y > 2):
        y = input("posY : ")
    tab[x][y] = char
    return tab

def main():
    row = 0
    tab = [".", ".", "."]
    tab[0] = ["1", "2", "3"]
    tab[1] = ["4", "5", "6"]
    tab[2] = ["7", "8", "9"]
    while(1 == 1):
        if row % 2 == 0:
            char = "X"
        else:
            char = "O"
        tab = assignTab(tab, char)
        printTab(tab)
        row += 1

main()
