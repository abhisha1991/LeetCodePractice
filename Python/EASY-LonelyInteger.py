# https://www.hackerrank.com/challenges/ctci-lonely-integer/problem
import sys
from collections import defaultdict

dict_a = defaultdict(int)


def lonely_integer(a):
    for i in a:
        dict_a[i] = dict_a[i] + 1

    for k, v in dict_a.items():
        if v == 1:
            return k


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
