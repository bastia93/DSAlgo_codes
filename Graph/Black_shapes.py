"""
Given character matrix A of O's and X's, where O = white, X = black.

Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)

"""

# make visited array
# if a index is black find bfs search and find all the black spots adjencent to this
# if white mark visited and go to next index

from collections import deque


def bfs(arr, m, n, visited, x, y):
    q = deque()
    visited[x][y] = False
    q.append([x, y])
    temp = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    while q:
        x,y = q.popleft()
        for i, j in temp:
            if 0 <= x + i < m and 0 <= y + j < n and visited[x + i][y + j]:
                visited[x + i][y + j] = False
                if arr[x + i][y + j] == "X":
                    q.append([x + i, y + j])

    return visited


def solve(A):
    m = len(A)
    n = len(A[0])

    vst = [[True for i in range(n)] for i in range(m)]



    ans = 0
    for i in range(m):
        for j in range(n):
            if vst[i][j]:
                if A[i][j] == "O":
                    vst[i][j] = False
                else:
                    ans += 1
                    vst = bfs(A, m, n, vst, i, j)

    return ans


A = [ "XXX", "OXO", "XOO" ]

print(solve(A))


"""
nicer Approach

solve(A):
    A = [list(row) for row in A]
    # Sounds like flood fill..
    def fill(row, col):
        if row < 0 or row >= len(A) or col < 0 or col >= len(A[row]) or A[row][col] != 'X':
            return
        A[row][col] = '-'
        fill(row-1, col)
        fill(row+1, col)
        fill(row, col-1)
        fill(row, col+1)
    count = 0
    for row in range(len(A)):
        for col in range(len(A[row])):
            char = A[row][col]
            if char == 'X':
                count += 1
                fill(row, col)
    return count
"""