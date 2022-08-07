def nextPermutation(A):
    n = len(A)

    curr = A[n - 1]
    index = -1
    for i in range(n - 2, -1, -1):
        if A[i] < curr:
            curr = A[i]
            index = i
            break
        else:
            if A[i] > curr:
                curr = A[i]

    if index == -1:
        return sorted(A)
    else:
        changeWith = max(A[index:])
        withIndex = A.index(changeWith)
        for i in range(index + 1, n):
            if A[i] > curr and A[i] < changeWith:
                changeWith = A[i]
                withIndex = i

        A[index] = changeWith
        A[withIndex] = curr

        A[index + 1:] = sorted(A[index + 1:])

        return A


print(nextPermutation([1, 2, 3]))
