"""
Given a matrix of integers A of size N x M . There are 4 types of squares in it:

1. 1 represents the starting square.  There is exactly one starting square.
2. 2 represents the ending square.  There is exactly one ending square.
3. 0 represents empty squares we can walk over.
4. -1 represents obstacles that we cannot walk over.

Find and return the number of 4-directional walks from
 the starting square to the ending square, that walk over every
 non-obstacle square exactly once.

"""

def solve(A):
    n = len(A)
    m = len(A[0])

    start = []
    end = []
    cell_count = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] == 1:
                start = [i, j]
            if A[i][j] == 2:
                end = [i, j]
            if A[i][j] == 0:
                cell_count += 1

    print(cell_count)
    def travel(x, y, count, ans):
        if x < 0 or x >= n or y < 0 or y >= m:
            return ans
        elif [x, y] == end:
            if count == cell_count:
                ans += 1
            return ans
        elif A[x][y] == -1:
            return ans
        else:
            A[x][y] = -1

            ans = travel(x+1, y, count + 1, ans)
            ans = travel(x-1, y, count+1, ans)
            ans = travel(x, y+1, count+1, ans)
            ans = travel(x, y-1, count+1, ans)
            A[x][y] = 0

            return ans

    out = travel(start[0], start[1], -1, 0)

    return out


A = [   [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, -1]   ]

print(solve(A))

