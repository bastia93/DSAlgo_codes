
# @param A : integer
# @param B : integer
# @param C : integer
# @param D : list of integers
# @param E : list of integers
# @param F : list of integers
# @param G : list of integers
# @param H : list of integers
# @return a list of integers
def solve(A, B, C, D, E, F, G, H):
    inf = 9999999

    distance = [[inf for i in range(A + 1)] for i in range(A + 1)]

    n = len(D)
    for i in range(n):
        distance[D[i]][E[i]] = F[i]
        distance[E[i]][D[i]] = F[i]

    for i in range(A + 1):
        distance[i][i] = 0
    print("the distance matrix before optimizing")
    for i in distance:
        print(i)
    for k in range(1, A + 1):
        for i in range(1, A + 1):
            for j in range(1, A + 1):
                if distance[i][j] > (distance[i][k] + distance[k][j]):
                    distance[i][j] = distance[i][k] + distance[k][j]
                    distance[j][i] = distance[i][k] + distance[k][j]

    # print(distance)
    ans = []
    print("After optimizing: ")
    for i in distance:
        print(i)


    for i in range(C):
        if distance[G[i]][H[i]] == inf:
            ans.append(-1)
        else:
            ans.append(distance[G[i]][H[i]])

    return ans

A = 4
B = 6
C = 2
D = [ 1, 2, 3, 2, 4, 3 ]
E = [ 2, 3, 4, 4, 1, 1 ]
F = [ 4, 1, 1, 1, 1, 1 ]
G = [ 1, 1 ]
H = [ 2, 3 ]

print(solve(A,B,C,D,E,F,G,H))
