def solve(A):
    hm = {
        ']' : '[',
        ')' : '(',
        '}' : '{'

    }
    stack = []
    n = len(A)
    arr = [0 for i in range(n+1)]

    for i in range(1,n+1):
        if not stack:

            stack.append([A[i-1], i])
        else:
            if A[i-1] in hm:
                if hm[A[i-1]] == stack[-1][0]:
                    arr[i] = 1 + arr[i-1] + 1 + arr[stack[-1][1]-1]
                    stack.pop()
                else:
                    stack.append([A[i-1], i])
                    arr[i] = 0
            else:
                stack.append([A[i-1], i])
                arr[i] = 0
    ans = 0
    for i in arr:
        ans = max(ans, i)

    return ans

X = '[]]'

print(solve(X))

