# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
from collections import defaultdict
import math

double_count = []


def number_needed(a, b):
    result = 0
    dicta = defaultdict(int)
    dictb = defaultdict(int)
    for i in a:
        dicta[i] += 1
    for i in b:
        dictb[i] += 1
    result += iterate_dict(dicta, dictb, True)
    result += iterate_dict(dictb, dicta, False)

    for i in double_count:
        result -= i

    return int(result)


def iterate_dict(dict_to_iterate, dict_to_compare, use_doublecount):
    result = 0
    for k, v in dict_to_iterate.items():
        if k in dict_to_compare.keys():
            diff = math.fabs(dict_to_iterate[k] - dict_to_compare[k])
            result = result + diff
            if use_doublecount:
                double_count.append(diff)
        else:
            result = result + dict_to_iterate[k]

    return result


#a = input().strip()
#b = input().strip()

print(number_needed("abcd", "axyz"))
