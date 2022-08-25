"""
A lucky number is a number that has exactly 2 distinct prime divisors.

You are given a number A,
and you need to determine the count of lucky numbers
between the range 1 to A (both inclusive).
"""


def solve(A):
    arr = [[i, set()] for i in range(A+1)]

    count = 0
    for i in range(2, A+1):
        if arr[i][0] == 1:
            if len(arr[i][1]) == 2:
                count += 1
        else:
            temp_number = arr[i][0]
            for j in range(i, A+1):
                if arr[j][0] % temp_number == 0:
                    arr[j][0] //= temp_number
                    arr[j][1].add(temp_number)

    return count


print(solve(50000))

