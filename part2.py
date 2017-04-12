#!/usr/bin/python3

def reachable(G, curCol, curRow):
    tempCol = curCol + 1
    tempRow = curRow
    move = 1
    i = tempRow + move
    points = []

    while(tempCol != Nc):
        while(i >= tempRow - move):
            print(i, tempCol)
            if(G[i][tempCol] == 1):
                points.append(tuple([i, tempCol]))
            i = i - 1
        move = move + 1
        tempCol = tempCol + 1

    return points

def findValue(value, curCol, curRow, valueList, Nc, G):
    points = reachable(G, curCol, curRow)
    for reachablePoint in points:
        findValue(value+1, reachablePoint[1], reachablePoint[0])
    if(curCol == Nc-1 or len(points) == 0):
        valueList.append(value)
        return valueList



if __name__ == '__main__':

    counter = 0
    Nr = 0
    Nc = 0
    targets = []

    with open('tmp') as f:
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

    grid = []
    for i in range(Nr):
        grid.append([])
        for j in range(Nc):
            grid[i].append(0)

    for aTuple in targets:
        grid[aTuple[0]][aTuple[1]] = 1

    valueList = []
    val = findValue(0, 0, (Nr/2)+1, valueList, Nc, grid)

    print(grid)
    print(val)
