# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem
t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    money = m
    list_ic = a
    num_ic = n
    i = 0
    '''
    2
    4
    5
    1 4 5 3 2
    '''
    length_ic = len(list_ic)
    for j in range(0, length_ic):
        diff = money - list_ic[j]
        if diff <= 0:
            continue
        elif j == 0:
            list_ic2 = list_ic[1:]
        elif j == length_ic - 1:
            list_ic2 = list_ic[:-1]
        else:
            list_ic2 = list_ic[0:j]
            list_ic2.extend(list_ic[j + 1:])
        if diff in list_ic2:
            # return indices
            k = list_ic.index(diff)
            if j == k:
                list_ic[k] = -1
                k = list_ic.index(diff)
            if j > k:
                print(k + 1, j + 1)
                break
            else:
                print(j + 1, k + 1)
                break






