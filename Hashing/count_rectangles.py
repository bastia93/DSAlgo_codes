"""
Given two arrays of integers A and B of size N each,
where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y)
in a 2-D Cartesian plane.

Find and return the number of unordered quadruplet
(i, j, k, l) such that (A[i], B[i]), (A[j], B[j]), (A[k], B[k]) and (A[l], B[l])
form a rectangle with the rectangle having all the sides parallel to either x-axis or y-axis.

"""


def solve(A, B):
    n = len(A)
    hash_set = set()

    for i in range(n):
        hash_set.add((A[i], B[i]))

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] == A[j] or B[i] == B[j]:
                continue
            if (A[i], B[j]) in hash_set and (A[j], B[i]) in hash_set:
                count += 1

    return count // 2
