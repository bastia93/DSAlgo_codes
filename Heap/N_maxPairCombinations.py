from heapq import heapify, heappop, heappush


def solve(A, B):
    A.sort()
    B.sort()

    n = len(A)
    heap = []
    heapify(heap)

    heappush(heap, [-(A[-1] + B[-1]), n-1, n-1])
    added_index = set()
    ans = []
    i = 0
    while i < n:
        temp = heappop(heap)
        max_sum = -temp[0]
        j = temp[1]
        k = temp[2]

        if (j, k) not in added_index:
            ans.append(max_sum)
            heappush(heap, [-(A[j - 1] + B[k]), j - 1, k])
            heappush(heap, [-(A[j] + B[k - 1]), j, k - 1])

            #set always take hashable objects, list is not a hashable object, so set takes tuple as element.
            added_index.add((j, k))
            i += 1
    return ans


A = [ 36, 27, -35, 43, -15, 36, 42, -1, -29, 12, -23, 40, 9, 13, -24, -10, -24, 22, -14, -39, 18, 17, -21, 32, -20, 12, -27, 17, -15, -21, -48, -28, 8, 19, 17, 43, 6, -39, -8, -21, 23, -29, -31, 34, -13, 48, -26, -35, 20, -37, -24, 41, 30, 6, 23, 12, 20, 46, 31, -45, -25, 34, -23, -14, -45, -4, -21, -37, 7, -26, 45, 32, -5, -36, 17, -16, 14, -7, 0, 37, -42, 26, 28 ]
B = [ 38, 34, -47, 1, 4, 49, -18, 10, 26, 18, -11, -38, -24, 36, 44, -11, 45, 20, -16, 28, 17, -49, 47, -48, -33, 42, 2, 6, -49, 30, 36, -9, 15, 39, -6, -31, -10, -21, -19, -33, 47, 21, 31, 25, -41, -23, 17, 6, 47, 3, 36, 15, -44, 33, -31, -26, -22, 21, -18, -21, -47, -31, 20, 18, -42, -35, -10, -1, 46, -27, -32, -5, -4, 1, -29, 5, 29, 38, 14, -22, -9, 0, 43 ]

print(solve(A, B))