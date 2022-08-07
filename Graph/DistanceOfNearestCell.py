from collections import deque


class Node:
    def __init__(self, node, level):
        self.index = node
        self.level = level


def find_lowest_cost():
    pass


def solve(A):
    inf = 999999
    q = deque()

    m = len(A)
    n = len(A[0])

    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                A[i][j] = inf
            else:
                A[i][j] = 0
                q.append(Node([i, j], 0))
    while q:
        temp = q.popleft()

        # Top
        x = temp.index[0] - 1
        y = temp.index[1]
        if 0 <= x < m and 0 <= y < n:
            if A[x][y] > temp.level + 1:
                A[x][y] = temp.level + 1
                temp2 = Node([x, y], temp.level + 1)
                q.append(temp2)

        # Bottom
        x = temp.index[0] + 1
        y = temp.index[1]
        if 0 <= x < m and 0 <= y < n:
            if A[x][y] > temp.level + 1:
                A[x][y] = temp.level + 1
                temp2 = Node([x, y], temp.level + 1)
                q.append(temp2)

        # Left
        x = temp.index[0]
        y = temp.index[1] - 1
        if 0 <= x < m and 0 <= y < n:
            if A[x][y] > temp.level + 1:
                A[x][y] = temp.level + 1
                temp2 = Node([x, y], temp.level + 1)
                q.append(temp2)

        # Right
        x = temp.index[0]
        y = temp.index[1] + 1
        if 0 <= x < m and 0 <= y < n:
            if A[x][y] > temp.level + 1:
                A[x][y] = temp.level + 1
                temp2 = Node([x, y], temp.level + 1)
                q.append(temp2)

    return A


X = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

Y = solve(X)
for i in Y:
    print(i)
