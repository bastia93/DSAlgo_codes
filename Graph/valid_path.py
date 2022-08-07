"""
There is a rectangle with left bottom as (0, 0) and right up as (x, y).

There are N circles such that their centers are inside the rectangle.

Radius of each circle is R. Now we need to find out
if it is possible that we can move from (0, 0) to (x, y) without touching any circle.

Note : We can move from any cell to any of
its 8 adjecent neighbours and we cannot move outside the boundary of
the rectangle at any point of time.

1st argument given is an Integer x ,
denoted by A in input.

2nd argument given is an Integer y,
denoted by B in input.

3rd argument given is an Integer N,
number of circles, denoted by C in input.

4th argument given is an Integer R,
radius of each circle, denoted by D in input.

5th argument given is an Array A of size N,
denoted by E in input, where A[i] = x cordinate of ith circle

6th argument given is an Array B of size N,
denoted by F in input, where B[i] = y cordinate of ith circle
"""
import math
from collections import deque


def is_in_circle(center, radius, point):
    lhs = math.pow(center[0] - point[0], 2) + math.pow(center[1] - point[1], 2)
    rhs = math.pow(radius, 2)

    if lhs <= rhs:
        return True
    else:
        return False


def create_map(arr, no_of_circles, x_cor, y_cor, radius):
    n = len(arr)
    m = len(arr[0])

    for i in range(no_of_circles):
        # create a square around the circle
        for j in range(-radius, radius + 1):
            for k in range(-radius, radius + 1):
                x = x_cor[i] + j
                y = y_cor[i] + k

                if 0 <= x < n and 0 <= y < m:
                    if arr[x][y]:
                        if is_in_circle([x_cor[i], y_cor[i]], radius, [x,y]):
                            arr[x][y] = False
    return arr


def solve(A, B, C, D, E, F):
    arr = [[True for i in range(B+1)] for i in range(A+1)]

    arr = create_map(arr, C, E, F, D)

    queue = deque()

    if arr[0][0]:
        queue.append([0, 0])
    else:
        return "NO"

    while queue:
        temp = queue.popleft()

        # Check the destination
        if temp[0] == A and temp[1] == B:
            return "YES"

        # Get all the 8 adjacent cells
        for i in range(-1, 2):
            for j in range(-1, 2):
                x = temp[0]+i
                y = temp[1]+j
                if 0 <= x <= A and 0 <= y <= B:
                    if arr[x][y]:
                        arr[x][y] = False
                        queue.append([x, y])

    return "NO"

x = 2
y = 3
N = 1
R = 1
A = [2]
B = [3]

print(solve(x,y,N,R,A,B))
