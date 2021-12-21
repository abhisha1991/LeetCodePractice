# https://www.youtube.com/watch?v=BysNXJHzCEs
# Very similar to longest common sub sequence - only difference is in if statement


def lcss(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    maxi = 0
    lcss_list = [[None] * (l2+1) for i in range(l1 + 1)]
    for i in range(l1 + 1):
        for j in range(l2 + 1):
            if i == 0 or j == 0:
                lcss_list[i][j] = 0

            elif str1[i - 1] == str2[j - 1]:
                lcss_list[i][j] = 1 + lcss_list[i-1][j-1]
                if maxi < lcss_list[i][j]:
                    maxi = lcss_list[i][j]

            else:
                lcss_list[i][j] = 0

    print(maxi)
    return maxi

# lcss("abcdaf", "zbcdf")

# Full program below


def longest_common_substr(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    i = 0
    j = 0
    lcs_list = []
    substr = []
    maxi = 0
    for x in range(l2 + 1):
        temp = [None] * (l1 + 1)
        lcs_list.append(temp)

    for i in range(0, l2 + 1):
        for j in range(0, l1 + 1):
            if i == 0 or j == 0:
                lcs_list[i][j] = 0

            elif str1[j - 1] == str2[i - 1]:
                lcs_list[i][j] = 1 + lcs_list[i - 1][j - 1]
                if lcs_list[i][j] > maxi:
                    maxi = lcs_list[i][j]
                    substr.append(str1[j - 1])

            else:
                lcs_list[i][j] = 0

    print(substr)
    return maxi


print(longest_common_substr('aaa', 'aabc'))
'''
test = int(input().strip())
for i in range(0, test):
    lens = [int(j) for j in input().strip().split(' ')]
    str1 = input().strip()
    str2 = input().strip()
    print(longestcommonsubstr(str1, str2))
'''