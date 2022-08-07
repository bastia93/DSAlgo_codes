from collections import deque


# find the adjencency arr
# Create visited arr
# Convert the weight 2 into three node by adding a dummy node (cost can be 1 or 2)
# BFS search for each edge save cost = 1
# when V node is found return total cost
# if not found and the queue becomes null return -1

# Create adjencency list
def solve(A, B, C, D):
    curr_node = A
    hm = {}

    def createAdjList(x, y):
        if x not in hm:
            hm[x] = []
        hm[x].append(y)
        if y not in hm:
            hm[y] = []
        hm[y].append(x)

    for fr, to, cost in B:
        if cost == 2:
            createAdjList(fr, curr_node)
            createAdjList(curr_node, to)
            curr_node += 1
        else:
            createAdjList(fr, to)

    vst = [-1 for i in range(curr_node)]
    print(hm)
    queue = deque()

    queue.append((C, 0))
    vst[C] = 1
    ans = 0

    # print(queue)
    while queue:

        node, level = queue.popleft()

        if node == D:
            return level
        if node in hm:

            for i in hm[node]:
                if vst[i] == -1:
                    vst[i] = 1
                    queue.append((i, level + 1))
        print(queue)
    return -1

A = 8
B =[
  [1, 7, 1],
  [4, 6, 2],
  [5, 7, 1],
  [6, 7, 1],
  [2, 5, 1],
  [1, 3, 2],
  [2, 3, 2],
  [0, 1, 2],
  [4, 5, 2],
  [1, 6, 1],
  [0, 6, 1]
]
C = 4
D = 0
x = solve(A,B,C,D)
print(x)