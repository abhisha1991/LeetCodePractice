# http://www.geeksforgeeks.org/knapsack-problem/


def knapsack(n, w, vals, wts):
    if n == 0 or w == 0:
        return 0
    '''
    wts =  1 2 4 5
    vals = 2 1 3 7
    w = 7
         0 1 2 3 4 5 6 7
    (2)1 0 2 2 2 2 2 2 2 
    (1)2 0 2 2 3 3 3 3 3 
    (3)4 0 2 2 2 3 5 5 6
    (7)5 0 2 2 2 3 7 9 9
    '''
    ks = []
    for i in range(n):
        temp = [None] * (w + 1)
        ks.append(temp)

    for i in range(n):
        for j in range(w + 1):
            if j == 0:
                ks[i][j] = 0
                continue

            if i == 0 and wts[i] > j:
                ks[i][j] = 0

            elif i == 0:
                ks[i][j] = vals[i]

            elif wts[i] > j:
                ks[i][j] = ks[i - 1][j]

            else:
                ks[i][j] = max(vals[i] + ks[i - 1][j - wts[i]], ks[i - 1][j])

    return ks[n - 1][w]


t = int(input().strip())
for i in range(0, t):
    n = int(input())
    w = int(input())
    vals = [int(x) for x in input().strip().split(' ')]
    wts = [int(x) for x in input().strip().split(' ')]
    print(knapsack(n, w, vals, wts))
