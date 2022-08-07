
def subsequences(A: list) -> int:
    ans = []

    def generate(A, idx, n, curr, ans):
        if idx == n:
            ans.append(curr)
            return ans
        else:
            # notchoose the element
            ans = generate(A,idx+1,n,curr, ans)
            ans = generate(A,idx+1,n, curr + [A[idx]], ans)
            return ans
    n = len(A)
    curr = []
    ans = generate(A, 0, n, curr, ans)

    return ans


if __name__ == "__main__":
    temp = subsequences([1,2,3])
    temp.sort()
    print(temp)
