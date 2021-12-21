def longest_palindromic_subseq(s):
    lens = len(s)
    arr = [[None] * lens for x in range(lens)]
    for i in range(lens):
        for j in range(lens):
            if i == j:
                arr[i][j] = 1

    i = 0
    l = 1
    j = l
    while l < lens:
        while j < lens:
            if s[i] == s[j]:
                arr[i][j] = 2 + int(arr[i+1][j-1])
            else:
                arr[i][j] = max(int(arr[i+1][j]), int(arr[i][j-1]))
            i += 1
            j += 1

        i = 0
        l += 1
        j = l

    return arr[0][lens - 1]

print(longest_palindromic_subseq('agbdba'))