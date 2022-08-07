"""
def solve(x: str) -> int:
    ans = 0
    currSum = 0

    end = -1

    n = len(x)

    for i in range(n):
        if x[i] == "1":
            currSum -= 1
        else:
            currSum += 1

        if currSum < 0:
            currSum = 0


        if currSum > ans:
            ans = currSum
            end = i

    return ans, end

A = "1101"
ans, endp = solve(A)

curr = 0
start = 0
for i in range(endp, -1, -1):

    if A[i] == "0":
        curr += 1
    else:
        curr -= 1

    if curr == ans:

        start = i


print(start+1, endp+1)

"""

def flip(A):

    n = len(A)
    ans = 0
    currSum = 0
    start = 0
    currStart = 0
    end = 0
    currEnd = 0

    for i in range(n):

        if A[i] == '1':
            print("I am here")
            currSum -= 1
        else:
            currSum += 1
        if currSum > ans:
            print("hello")
            start = currStart
            ans = currSum
            end = i

        if currSum < 0:
            currSum = 0
            currStart = i+1

    return [start, end]

print(flip("1001000010001"))