#!/usr/bin/python3

def reachable(G, curCol, curRow, Nc, Nr):
    tempCol = curCol + 1
    tempRow = curRow
    move = 1
    points = []

    while(tempCol != Nc):
        i = tempRow + move
        if(i > Nr-1):
            i = Nr-1
        while(i >= tempRow - move):
            if(i < 0):
                break
            print(i, tempCol)
            if(G[i][tempCol] == 1):
                points.append(tuple([i, tempCol]))
            i = i - 1
            move = move + 1
        tempCol = tempCol + 1

    return points

def findValue(value, curCol, curRow, valueList, Nc, G, Nr):
    points = reachable(G, curCol, curRow, Nc, Nr)
    for reachablePoint in points:
        findValue(value+1, reachablePoint[1], reachablePoint[0], valueList, Nc, G, Nr)
    if(curCol == Nc-1 or len(points) == 0):
        valueList.append(value)

    return valueList



if __name__ == '__main__':

    counter = 0
    Nr = 0
    Nc = 0
    targets = []

#Read in Nr, Nc, and target coordinates from the file
    with open('in01.txt') as f:
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

#Find the max value from the valueList, which should be the max targets hit in an optimum route
    valueList = []
    valueList = findValue(0, 0, (Nr/2)+1, valueList, Nc, grid, Nr)
    maxVal = max(valueList)
    print
    print(valueList)
    print
    print(maxVal)
