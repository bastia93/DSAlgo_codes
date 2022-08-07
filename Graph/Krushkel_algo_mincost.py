def solve(A, B):
    c = sorted(B, key=lambda x: x[2])

    parent_arr = [i for i in range(A + 1)]
    ans = 0

    def find_parent(x):
        if parent_arr[x] != x:
            parent_arr[x] = find_parent(parent_arr[x])
            return parent_arr[x]
        return x

    for fr, to, cost in c:
        parent_fr = find_parent(fr)
        parent_to = find_parent(to)

        if parent_fr != parent_to:
            ans += cost
            parent_arr[parent_to] = parent_fr
    return ans


A = 4
B = [[1, 2, 1],
     [2, 3, 4],
     [1, 4, 3],
     [4, 3, 2],
     [1, 3, 10]]

print(solve(A, B))
