# https://www.hackerrank.com/challenges/ctci-ransom-note/problem
from collections import defaultdict


def ransom_note(magazine, ransom):
    len_ransom = len(ransom)
    count = 0
    dict_mag = defaultdict(list)
    for j in magazine:
        dict_mag[j].append(j)
    for i in ransom:
        if i in dict_mag.keys():
            if (len(dict_mag[i]) > 0):
                dict_mag[i].remove(i)
                count += 1
            else:
                return False

    return count == len_ransom


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if answer:
    print('Yes')
else:
    print('No')
