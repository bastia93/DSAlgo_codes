"""
Given a matrix of integers A of size N x M describing a maze.
The maze consists of empty locations and walls.

1 represents a wall in a matrix and 0 represents an empty location in a wall.

There is a ball trapped in a maze. The ball can go through empty spaces by rolling up, down,
left or right, but it won't stop rolling until hitting a wall (maze boundary is also considered
as a wall). When the ball stops, it could choose the next direction.

Given two array of integers of size B and C of size 2 denoting the starting and
destination position of the ball.

Find the shortest distance for the ball to stop at the destination.
The distance is defined by the number of empty spaces traveled by the ball from
the starting position (excluded) to the destination (included).
If the ball cannot stop at the destination, return -1.

"""

from collections import deque


def solve(A, B, C):

    n = len(A)
    m = len(A[0])

    dict_direction = {0: [1, 0], 1: [-1, 0], 2: [0, 1], 3: [0, -1]}

    vst = [[[True for i in range(4)] for i in range(m)] for i in range(n)]

    queue = deque()

    def wall_ahead(cell):

        if 0 <= cell[0] < n and 0 <= cell[1] < m:

            if A[cell[0]][cell[1]] == 1:
                return "yes"
            else:
                return "no"
        else:
            return "yes"

    def change_direction(cell, level):
        for key, value in dict_direction.items():
            if wall_ahead([cell[0] + value[0], cell[1] + value[1]]) == "no" and \
                    vst[cell[0] + value[0]][cell[1] + value[1]][key]:
                queue.append([cell[0] + value[0], cell[1] + value[1], key, level + 1])

    # from destination add all possible paths
    change_direction(B, 0)

    # Pop one cell and all possible adjencent cells
    while queue:
        temp = queue.popleft()

        # first mark visited
        vst[temp[0]][temp[1]][temp[2]] = False

        # 2nd Check is this your ans
        if temp[0:2] == C and wall_ahead(
                [temp[0] + dict_direction[temp[2]][0], temp[1] + dict_direction[temp[2]][1]]) == "yes":
            return temp[3]

        else:
            if wall_ahead([temp[0] + dict_direction[temp[2]][0], temp[1] + dict_direction[temp[2]][1]]) == "yes":
                change_direction(temp[0:2], temp[3])
            else:
                queue.append(
                    [temp[0] + dict_direction[temp[2]][0], temp[1] + dict_direction[temp[2]][1], temp[2], temp[3] + 1])

    return -1


A = [ [0, 0], [0, 1] ]
B = [0, 0]
C = [0, 1]

print(solve(A, B, C))