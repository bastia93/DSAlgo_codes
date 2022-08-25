"""
Given two arrays of integers A and B of size N each,
where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane.

Find and return the number of unordered triplets (i, j, k)
such that (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right-angled
triangle with the triangle having one side parallel to the x-axis and one side
parallel to the y-axis.

"""


def solve(A, B):

    y_coordinate = {}
    x_coordinate = {}

    n = len(A)
    ans = 0
    for i in range(n):
        if A[i] not in x_coordinate:
            x_coordinate[A[i]] = 0
        x_coordinate[A[i]] += 1
        if B[i] not in y_coordinate:
            y_coordinate[B[i]] = 0
        y_coordinate[B[i]] += 1

    for i in range(n):
        m = x_coordinate[A[i]]
        p = y_coordinate[B[i]]

        ans += (m-1) * (p-1)
    return ans % (10**9 + 7)

