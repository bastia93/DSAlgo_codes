def find_minimum_multiplication(arr: list):
    n = len(arr)
    if n < 3:
        return 0
    if n == 3:
        return arr[0] * arr[1] * arr[2]

    dp = [[99999 for i in range(n)] for i in range(n)]

    for i in range(1, n):
        for j in range(1, n):
            if i == j:
                dp[i][j] = 0
            else:

                for k in range(i,j):
                    dp[i][j] = min(dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j], dp[i][j])

    for i in dp:
        print(i)
    return "Hello"
A= [3,5,7]

print(find_minimum_multiplication(A))