"""
from heapq import heapify, heappop, heappush


def solve(A, B):
    n = len(A) + 1
    m = len(B) + 1

    visited = [[True for i in range(m)] for i in range(n)]

    total_cost = 0
    heap = []
    heapify(heap)
    visited[0][0] = False
    heappush(heap, [A[0], [1, 0]])
    heappush(heap, [B[0], [0, 1]])

    while heap:
        cost, coordinate = heappop(heap)
        x, y = coordinate[0], coordinate[1]
        if visited[x][y]:
            visited[x][y] = False
            total_cost += cost


        # top
        if 0 <= x - 1 < n and 0 <= y < m:
            if visited[x - 1][y]:
                heappush(heap, [A[x - 1], [x - 1, y]])

            # Bottom
        if 0 <= x + 1 < n and 0 <= y < m:
            if visited[x + 1][y]:
                heappush(heap, [A[x], [x + 1, y]])

            # right
        if 0 <= x < n and 0 <= y + 1 < m:
            if visited[x][y + 1]:
                heappush(heap, [B[y], [x, y + 1]])

            # Left
        if 0 <= x < n and 0 <= y - 1 < m:
            if visited[x][y - 1]:
                heappush(heap, [B[y - 1], [x, y - 1]])

    return total_cost

"""

def solve_2(A, B):
    n = len(A)
    m = len(B)
    arr = []
    for i in A:
        arr.append([i, 0])
    for j in B:
        arr.append([j, 1])

    arr.sort()
    print(arr)
    n += 1
    m += 1
    total_cost = 0

    for cost, identifier in arr:
        if identifier == 0:
            total_cost += cost * m
            n -= 1

        else:
            total_cost += cost * n
            m -= 1
        print(m,n)

    return total_cost % (10**9 + 7)



A = [ 2, 2, 4, 1, 2, 4, 2 ]
B = [ 3, 3, 4, 5 ]
print(solve_2(A,B))