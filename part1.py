#!/usr/bin/python3
import sys

def isReachable(G, curRow, curCol, Nr, Nc):
    counter = 1
    curCol = curCol + 1
    for col in xrange(curCol, Nc):
        bottom = curRow + counter
        top = curRow - counter

        if(bottom > Nr-1):
            bottom = Nr-1
        if(top < 0):
            top = 0

        for row in xrange(top, bottom+1):
            print(row, col)
            if(G[row][col] == 1):
                return col

        counter = counter + 1

    return False











if __name__ == '__main__':

    counter = 0
    Nr = 0
    Nc = 0
    targets = []

#Read in Nr, Nc, and target coordinates from the file

    filename = sys.argv[1]
    with open(filename) as f:
        for l in f:
            if counter == 0:
                tempR, tempC = l.split()
                Nr = int(tempR)
                Nc = int(tempC)
                counter = counter + 1
            else:
                tempX, tempY = l.split()
                x = int(tempX)
                y = int(tempY)
                tempCoords = tuple([x,y])
                targets.append(tempCoords)

#Initialize the 2D grid
    grid = []
    for i in range(Nr):
        grid.append([])
        for j in range(Nc):
            grid[i].append(0)

#Set targets to 1 in the grid
    for aTuple in targets:
        grid[aTuple[0]][aTuple[1]] = 1

    move = ""
    pos = tuple([Nr/2, 0])


    print(isReachable(grid, 1, 1, Nr, Nc))
