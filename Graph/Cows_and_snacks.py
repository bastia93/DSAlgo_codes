def solve(A: int, B: list[int]) -> int:
    parent = [i for i in range(A)]
    sad_guest = 0

    def find_parent(node):
        if node == parent[node]:
            return node
        else:
            parent[node] = find_parent(parent[node])
            return parent[node]

    for x, y in B:
        parent_x = find_parent(x)
        parent_y = find_parent(y)

        if parent_x == parent_y:
            sad_guest += 1
        else:
            #important point
            # don't change the parent change parent of parent
            parent[parent_y] = parent_x



    return sad_guest


A = 100000
B = [
    [8, 7],
    [1, 9],
    [5, 4],
    [11, 12],
    [7, 8],
    [3, 4],
    [3, 5],
    [12, 15],
    [15, 13],
    [13, 14]]
print(solve(A,B))