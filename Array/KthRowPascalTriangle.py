def solve(A):
    factorialArr = [1 for i in range(A+1)]

    for i in range(1,A+1):
        factorialArr[i] = factorialArr[i-1] * i

    ans = []

    for i in range(A+1):
        temp = factorialArr[A]//(factorialArr[A-i] * factorialArr[i])
        ans.append(temp)

    print(ans)

