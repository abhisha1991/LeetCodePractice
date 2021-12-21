# http://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/
def largest_seq(matrix, n):
    maxi = -1
    pos = (-1, -1)
    for i in range(n):
        for j in range(n):
            if maxi < matrix[i][j]:
                maxi = matrix[i][j]
                pos = (i, j)

    result = []
    while maxi > 0 and pos[0] != -1:
        print("Finding ", maxi)
        result.append(matrix[pos[0]][pos[1]])
        xy = get_nbors(pos, n)
        # print(xy)
        maxi -= 1
        p = number_less_than_one(matrix, xy, maxi)
        if p is None:
            break

        pos = p

    return list(reversed(result))


def number_less_than_one(matrix, xy, target):
    # print("Target", target)
    for p in xy:
        # print("p is", p)
        if matrix[p[0]][p[1]] == target:
            return p

    return None


def get_nbors(pos, n):
    xy = []
    i = pos[0]
    j = pos[1]
    if i < n and j + 1 < n:
        xy.append((i, j + 1))
    if i < n and j - 1 >= 0:
        xy.append((i, j - 1))
    if i + 1 < n and j < n:
        xy.append((i + 1, j))
    if i - 1 >= 0 and j < n:
        xy.append((i - 1, j))

    return xy


t = int(input())
for i in range(t):
    n = int(input())
    mat = [int(x) for x in input().strip().split(' ')]
    matrix = []
    j = 0
    k = 0
    temp = []
    while len(matrix) != n:
        if j == n:
            j = 0
            matrix.append(temp)
            temp = []
        if j < n and len(matrix) != n:
            print(mat[k])
            temp.append(mat[k])
            k += 1
            j += 1
    print(matrix)
    x = largest_seq(matrix, n)
    print(x)
