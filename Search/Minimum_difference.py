"""
You are given a 2-D matrix C of size A × B.
You need to build a new 1-D array of size A by taking one element from each row of the 2-D matrix in such a way that the cost of the newly built array is minimized.

The cost of an array is the minimum possible value of the absolute difference between any two adjacent elements of the array.

So if the newly built array is X, the element picked from row 1 will become X[1], element picked from row 2 will become X[2], and so on.

Determine the minimum cost of the newly built array.

"""


def binary_search(number, arr):
    """
    Given a number find the nearest greater number in the array.
    """
    start = 0
    end = len(arr)-1

    while(start< end):
        mid = (start + end) // 2

        if arr[mid] < number:
            start += 1
        else:
            end = mid

    return end


def solve(A: int, B: int, C: list[list[int]]) -> int:
    ans = 99999


    for i in range(A-1):
        for j in range(B):
            greater_index = binary_search(C[i][j], C[i+1])
            if greater_index != 0:
                ans = min(ans, abs(C[i][j] - C[i+1][greater_index]), abs(C[i][j] - C[i+1][greater_index-1]))
            else:
                ans = min(ans, abs(C[i][j] - C[i + 1][greater_index]))

    return ans


A = 10
B = 10
C = [
  [95171, 64925, 51398, 40114, 693, 2377, 73808, 80091, 76151, 79440],
  [67162, 89457, 65239, 89157, 31092, 37848, 22896, 30167, 37883, 36897],
  [5988, 77161, 72711, 64765, 26452, 77921, 9225, 96615, 24939, 45282],
  [22835, 8357, 10207, 74133, 36619, 98949, 64658, 10426, 79039, 29057],
  [89767, 34448, 18513, 43253, 23604, 37753, 81001, 34649, 67820, 7132],
  [59694, 73708, 84193, 32404, 26720, 98793, 98473, 35846, 83656, 11659],
  [69276, 6490, 19916, 67631, 68771, 56435, 66579, 33428, 66762, 45617],
  [50633, 44776, 68213, 69046, 87929, 79966, 6799, 68930, 2862, 62767],
  [75962, 62456, 24723, 48402, 83008, 51343, 35443, 69728, 87089, 19098],
  [81288, 44613, 13736, 1203, 12243, 70655, 45787, 78723, 92231, 12548]
]
print(solve(A, B, C))