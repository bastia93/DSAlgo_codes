"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message denoted by string A containing digits, determine the total number of ways to decode it modulo 109 + 7.

"""

def solve(A: str):
    arr = []

    n = len(A)

    for i in range(n):
        if A[i] == '0':

            if 0 < arr[-1] < 3:
                arr[-1] *= 10
            else:
                return 0
        else:
            arr.append(int(A[i]))
    print(arr)
    n = len(arr)+ 1

    dp = [0 for i in range(n)]
    dp[1] = 1
    for i in range(2,n):
        dp[i] += dp[i-1]

        if (int(str(arr[i-2])+str(arr[i-1]))) < 27:
            dp[i] += max(1, dp[i-2])


    return dp[-1] % (10**9 + 7)




x = '2611055971756562'
print(solve(x))
