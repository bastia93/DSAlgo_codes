from heapq import heapify, heappop, heappush


def solve(row: int, column: int, matrix: list[list[int]]):
    visited = [[True for i in range(column)] for i in range(row)]

    heap = []

    heapify(heap)
    abs_difference = 0
    heappush(heap, [0, [0, 0]])

    counter = 0

    adj_indices = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while counter < row * column:

        temp_difference, co_ordinate = heappop(heap)
        x_place = co_ordinate[0]
        y_place = co_ordinate[1]

        if visited[x_place][y_place]:
            visited[x_place][y_place] = False
            counter += 1
            abs_difference = max(abs_difference, temp_difference)

            for x, y in adj_indices:
                if 0 <= x_place + x < row and 0 <= y_place + y < column and visited[x_place + x][y_place + y]:
                    heappush(heap, [abs(matrix[x_place + x][y_place + y] - matrix[x_place][y_place]),
                                    [x_place + x, y_place + y]])

    return abs_difference


A = 3
B = 3
C = [[1, 5, 6],
     [10, 7, 2],
     [3, 6, 9]]

print(solve(A, B, C))
