'''
Super simple, - was asked this question in AI&R
'''


def find_all_permutations(n):
    roll('', n)


def roll(s, n):
    if n == 0:
        print(s)
    else:
        for i in range(1, 7):
            roll(s + ',' + str(i), n-1)

find_all_permutations(4)