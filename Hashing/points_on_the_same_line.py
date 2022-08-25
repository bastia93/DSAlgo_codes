"""
Given two arrays of integers A and B describing a pair of (A[i], B[i])
coordinates in a 2D plane. A[i] describe x coordinates of the ith point in the 2D plane,
whereas B[i] describes the y-coordinate of the ith point in the 2D plane.

Find and return the maximum number of points that lie on the same line.

"""


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def solve(A, B):
    n = len(A)
    max_points = 0

    for i in range(n):
        temp_hash = {}
        same_points = 0
        temp_max = 0
        for j in range(i + 1, n):
            num = B[j] - B[i]
            den = A[j] - A[i]
            if num == 0 and den == 0:
                same_points += 1
                continue

            hcf = gcd(num, den)

            num //= hcf
            den //= hcf

            if (num, den) not in temp_hash:
                temp_hash[(num, den)] = 0
            temp_hash[(num, den)] += 1

            temp_max = max(temp_max, temp_hash[(num, den)])

        max_points = max(max_points, temp_max + same_points)

    return max_points + 1

A = [ 48, 45, -3, 7, -25, 38, 2, 13, 13, 18, -44, 34, -27, -46, 48, -39, -41, -32, -16, 17, -6, 44, -28, -44, -6, -43, -16, 30, -3, -27, 32, 38, -26, 20, 4, -44, -37 ]
B = [ 47, -42, 41, 22, -4, -35, -45, -22, 5, -20, 21, -13, 47, 32, -48, 47, 17, -23, 30, -30, 37, 42, 44, 23, 1, -40, -9, 34, -34, 49, 16, -35, 2, -19, 31, 23, -37 ]

print(solve(A,B))