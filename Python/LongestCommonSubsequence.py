# http://practice.geeksforgeeks.org/problems/longest-common-subsequence/0
# http://www.geeksforgeeks.org/longest-common-subsequence/
# https://www.youtube.com/watch?v=NnD96abizww
import math


def lcs(str1, str2):

    l1 = len(str1)
    l2 = len(str2)
    # declaring the array for storing the dp values
    lcs_list = [[None] * (l2 + 1) for k in range(l1 + 1)]

    for i in range(l1 + 1):
        for j in range(l2 + 1):
            if i == 0 or j == 0:
                lcs_list[i][j] = 0
            elif str1[i-1] == str2[j-1]: # comparing forwards, not backwards
                lcs_list[i][j] = 1 + lcs_list[i-1][j-1]
            else:
                lcs_list[i][j] = math.max(lcs_list[i - 1][j], lcs_list[i][j - 1])
    return lcs_list[l1][l2]


lcs("AAAA", "AAAAA")

# The below is a wrong solution - btw, as a side note, it does a backward comparison
res = 0


def lcs2(str1, str2):
    global res

    i = len(str1) - 1
    j = len(str2) - 1
    print("i is ", i)
    print("j is ", j)

    if i < 0 or j < 0:
        return 0

    while i >= 0 and j >= 0:
        equal = str2[j] == str1[i]
        if equal:
            res += 1 + lcs2(str1[:i], str2[:j])
        else:
            res += max(lcs2(str1[:i + 1], str2[:j]),
                       lcs2(str1[:i], str2[:j + 1]))


x = map(int, input().strip().split(' '))
for i in x:
    ip = input().strip().split(' ')
    y = [int(z) for z in ip]
    str1 = input().strip()
    str2 = input().strip()
    assert (y[0] == len(str1))
    assert (y[1] == len(str2))
    print(y[0])
    print(y[1])
    lcs(str1, str2)

    print(res)

