
def solve(A, B, C):
    arr = [[i, -1] for i in range(A+1)]

    def find_parent(index):
        if index == arr[index][0]:
            return index
        else:
            arr[index][0] = find_parent(arr[index][0])
            return arr[index][0]

    for i, j in B:
        if i > j:
            i, j = j, i
        parent_i = find_parent(i)
        parent_j = find_parent(j)
        arr[parent_j][0] = parent_i
        arr[i][1] = 0
        arr[j][1] = 0

    for i in range(1, A+1):
        arr[i][0] = find_parent(i)

    for i, j in C:
        if i > j:
            i, j = j, i
        if arr[i][0] != arr[j][0]:
            if arr[i][1] != 0 and arr[j][1] != 0:
                parent_i = find_parent(i)
                parent_j = find_parent(j)
                arr[parent_j][0] = parent_i
                arr[i][1] = 1
                arr[j][1] = 1
            else:
                return 0

    for i in range(1, A+1):
        arr[i][0] = find_parent(i)

    ans = set()
    for i in range(1, A+1):
        ans.add(arr[i][0])

    n = len(ans)

    return (2**n) % (10**9 + 7)


A = 4
B = [
   [1, 2], [1,4]
 ]
C = [
   [4, 3]
 ]

print(solve(A,B,C))


