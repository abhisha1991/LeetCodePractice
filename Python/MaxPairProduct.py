# https://codefights.com/interview/AeoqA9TH3CSk9HqkH
import math


def maxPairProduct(a):
    if a is []:
        return -1

    a.sort()
    for i in range(len(a) - 1, 1, -1):
        if 1 in a:
            return a[len(a)-1]
        b = a[0: i]
        target = a[i]
        for j in range(0, len(b)):
            if target % b[j] == 0:
                c = b[:]
                del c[j]
                quotient = int(target / b[j])
                if quotient in c:
                    return target

    return -1


def maxPairProduct2(a):
    if a is []:
        return -1

    a.sort()
    for i in range(len(a) - 1, 0, -1):
        target = a[i]
        # has to be a product of 2 numbers
        if i is 0 or i is 1:
            return -1
        b = []
        sqrt_target = math.sqrt(target)
        is_sqrt_target_int = False
        if type(sqrt_target) is int:
            is_sqrt_target_int = True
        for j in range(1, target + 1):
            if j in a:
                add_j_count_times = [j] * a.count(j)
                b.extend(add_j_count_times)
                if is_sqrt_target_int and any((b.count(x) == 2) and (x * x == target) for x in b):
                    return target
                if any((y != x) and (b[y] * b[x]) == target for x in range(0, len(b)) for y in range(0, len(b))):
                    return target

    return -1


print(maxPairProduct([88, 57, 44, 92, 28, 66, 60, 37, 33, 52, 38, 29, 76, 8, 75]))


'''
# print(maxPairProduct([4, 1, 82, 48, 39, 60, 52, 36, 35, 40, 93, 16, 28, 5, 30, 50, 65, 86, 30, 44, 36, 78, 1, 39, 72, 
50, 90, 68, 89]))

print(maxPairProduct([51, 80, 91, 55, 51, 32, 14, 58, 95, 82, 82, 4, 21, 34, 83, 82, 88, 16, 97, 26, 5, 23, 93, 52, 98,
                      33, 35, 82, 7, 16, 58, 9, 96, 100, 63, 98, 84, 77, 55, 78, 10, 88, 33, 83, 22, 67, 64, 61, 83, 12,
                      86, 87, 86, 31, 91, 84, 15, 77, 17, 21, 93, 26, 29, 40, 26, 91, 37, 61, 19, 44, 38, 29, 83, 22,
                      11, 56]))
'''


