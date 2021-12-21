# code
from collections import defaultdict
import math

# https://www.youtube.com/watch?v=We3YDTzNXEk
# A Dynamic Programming based Python program for edit
# distance problem
def editDistDP(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]


# Driver program
str1 = "sunday"
str2 = "saturday"

print(editDistDP(str1, str2, len(str1), len(str2)))


# wrong solution
dict_str1 = defaultdict(list)
dict_str2 = defaultdict(list)


def convert_str(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    for idx, i in enumerate(str1):
        dict_str1[i].append(idx)

    for idx, i in enumerate(str2):
        dict_str2[i].append(idx)

    result = 0
    for k, v in dict_str2.items():
        if k in dict_str1.keys():
            temp = dict_str1[k]
            if sorted(temp) == sorted(v):
                continue
            # handle insert/delete
            result += abs(len(v) - len(temp))
            # handle replace
            for i in temp:
                if i not in v:
                    result += 1
        if k not in dict_str1.keys():
            result += len(dict_str2[k])
    return result


convert_str("geek", "gesek")

# input
ip = int(input().strip())
for i in range(0, ip):
    lens = [int(l) for l in input().strip().split(' ')]
    ips = [l for l in input().strip().split(' ')]
    str1 = ips[0]
    str2 = ips[1]
    print(convert_str(str1, str2))

