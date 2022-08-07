"""
 students applied for admission in IB Academy. An array of integers B is given representing the strengths of A people i.e. B[i] represents the strength of ith student.

Among the A students some of them knew each other. A matrix C of size M x 2 is given which represents relations where ith relations depicts that C[i][0] and C[i][1] knew each other.

All students who know each other are placed in one batch.

Strength of a batch is equal to sum of the strength of all the students in it.

Now the number of batches are formed are very much, it is impossible for IB to handle them. So IB set criteria for selection: All those batches having strength at least D are selected.

Find the number of batches selected.

NOTE: If student x and student y know each other, student y and z know each other then student x and student z will also know each other.


"""


def solve(students: int, strength: list[int], relation: list[list[int]], criteria: int) -> int:
    parent = [i for i in range(students)]

    def find_parent(node):
        if parent[node] == node:
            return node
        else:
            parent[node] = find_parent(parent[node])
            return parent[node]

    for i, j in relation:
        parent_i = find_parent(i - 1)
        parent_j = find_parent(j - 1)

        parent[parent_j] = parent_i

    for i in range(students):
        parent[i] = find_parent(i)

    hm = {}

    for i in range(students):
        if parent[i] not in hm:
            hm[parent[i]] = 0
        hm[parent[i]] += strength[i]

    ans = 0

    for i in hm:
        if hm[i] >= criteria:
            ans += 1

    return ans


A = 5
B = [1, 2, 3, 4, 5]
C = [[1, 5],
     [2, 3]]
D = 6

print(solve(A, B, C, D))
