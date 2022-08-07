def generate(A, ind, n, curr, ans):
    if ind == n:
        ans.append(curr)
        return ans

    else:
    # not choose the element
        ans = generate(A, ind + 1, n, curr, ans)
        #ans.append(temp)
        # choose the element
        ans = generate(A, ind + 1, n, curr + [A[ind]], ans)
        #ans.append(temp)

    return ans
A = [1, 2, 3]
ans = []
n = len(A)
ind = 0
curr = []

ans = generate(A, ind, n, curr, ans)

ans.sort()
print(ans)