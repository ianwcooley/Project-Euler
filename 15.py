# Project Euler problem 15: Starting at the top left-corner and ending at the
# bottom-right, find the number of paths through a 20-20 lattice, only moving
# left and down.

numRows = 20
numCols = 20

numWaysMemory = []
for i in range(0, numRows):
    numWaysMemory.append([])
    for j in range(0,numCols):
        numWaysMemory[i].append(None)


def numWays(m,n):
    if m == 0 or n == 0:
        return 1
    elif numWaysMemory[m-1][n-1] != None:
        return numWaysMemory[m-1][n-1]
    
    else:
        num = numWays(m - 1 ,n) + numWays(m,n - 1)
        numWaysMemory[m-1][n-1] = num
        return num

print(numWays(20,20))


