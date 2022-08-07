def solve(A, B, C, D):
    pre_sum = []

    n = len(A)
    pre_sum.append(B*A[0])
    for i in range(1,n):
        pre_sum.append(max(pre_sum[-1], B*A[i]))

    #print(f"pre sum 1: {pre_sum}")
    # pre_sum 2

    pre_sum[0] = pre_sum[0] + C*A[0]

    for i in range(1, n):
        pre_sum[i] = max(pre_sum[i] + A[i]*C, pre_sum[i-1])

    #print(f"pre sum 2: {pre_sum}")
    # pre_sum 3
    pre_sum[0] = pre_sum[0] + D * A[0]

    for i in range(1, n):
        pre_sum[i] = max(pre_sum[i] + A[i] * D, pre_sum[i-1])

    #print(f"pre sum 3: {pre_sum}")

    return pre_sum[-1]

A = [1, 5, -3, 4, -2]
B = 2
C = 1
D = -1

print(solve(A,B,C,D))

