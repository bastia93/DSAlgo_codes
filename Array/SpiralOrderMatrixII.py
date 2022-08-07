"""
Given an integer A,
generate a square matrix filled with elements from 1 to A2 in spiral order.

"""

def solve(A):
    matrix = [[0 for i in range(A)] for i in range(A)]

    startCol = 0
    endCol = A-1

    startRow = 0
    endRow = A-1

    counter = 1
    while startRow <= endRow and startCol <= endCol:

        # Left to right same row
        for i in range(startCol,endCol+1,1):
            matrix[startRow][i] = counter
            counter += 1
        startRow += 1

        # Top to Bottom
        for i in range(startRow,endRow+1,1):
            matrix[i][endCol] = counter
            counter += 1
        endCol -= 1

        # Right to left
        for i in range(endCol,startCol-1, -1):
            matrix[endRow][i] = counter
            counter += 1
        endRow -= 1

        # Bottom to Top
        for i in range(endRow, startRow-1, -1):
            matrix[i][startCol] = counter
            counter += 1
        startCol += 1

    return matrix

temp = solve(5)

for i in temp:
    print(i)
