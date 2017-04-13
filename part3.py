#!/usr/bin/python3
import sys

def findValue(G, Nr, Nc, T, E): #G, Nr,Nc,T,E
    if (T[curRow][curCol] == -1):    #hasn't been checked

        if (curCol == Nc):
            T[curRow][curCol] = 0

        else:
            #up
            t1 = findValue2(value, curCol+1, curRow-1, valueList, Nc, G, Nr)
            #straight
            t2 = findValue2(value, curCol+1, curRow, valueList, Nc, G, Nr)
            #down
            t3 = findValue2(value, curCol+1, curRow+1, valueList, Nc, G, Nr)

            maxVal = max(t1, t2, t3)
            if(maxVal == t1):
                T[curRow][curCol] = t1
                E[curRow][curCol] = 1
            elif(maxVal == t2):
                T[curRow][curCol] = t2
                E[curRow][curCol] = 2
            else:
                T[curRow][curCol] = t3
                E[curRow][curCol] = 3
    return T[curRow][curCol]

def findValue2(value, curCol, curRow, valueList, Nc, G, Nr):
    points = reachable(G, curCol, curRow, Nc, Nr)
    for reachablePoint in points:
        findValue2(value+1, reachablePoint[1], reachablePoint[0], valueList, Nc, G, Nr)
        if(curCol == Nc-1 or len(points) == 0):
            valueList.append(value)
    return max(valueList)



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

    #Initialize 2D table 'T'
    T = []
    for i in range(Nr):
        T.append([])
        for j in range(Nc):
            T[i].append(-1)

    #Initialize 2D table 'E'
    E = []
    for i in range(Nr):
        E.append([])
        for j in range(Nc):
            E[i].append(-1)



    #Set targets to 1 in the grid
    for aTuple in targets:
        grid[aTuple[0]][aTuple[1]] = 1

    #Find the max value from the valueList, which should be the max targets hit in an optimum route

    valueList = []
    valueList = findValue(grid, Nr, Nc, T, E)
    maxVal = max(valueList)

    print(maxVal)

    print

    n = maxVal
    A = ""

    t = E[Nr-1][Nc-1]
    while(t != -1):
        if(t == 1):
            A = A + "U"
        elif(t == 2):
            A = A + "S"
        else:
            A = A + "D"

    print(A[::-1])
