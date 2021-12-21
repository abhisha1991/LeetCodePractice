# https://www.youtube.com/watch?v=WxpIHvsu1RI
# this problem is very similar to partition problem

'''
the second player is attempting to use the same optimal strategy as player one. So, after player one picks from the
left most or right most entry, player two will have the opportunity to attempt to maximize their return.

The values stored in the array are are stored in pairs where the first value in the pair is the maximum
value that the person currently picking can get and the second value is the maximum value that the
person going after can get. Since it's player two's turn at that point,
the player will naturally grab the first value in the pair and the player one, who will be the next one
to go will be forced to grab the second value in the pair.﻿
'''


def optimal_strategy(arr):
    len_arr = len(arr)
    res = [[None] * len_arr for x in range(len_arr)]

    l = 1
    for i in range(len_arr):
        for j in range(len_arr):
            # there's only 1 number in the game
            if i == j:
                # first player always wins by picking up the number, as a result player 2 gets nothing
                res[i][j] = (arr[i], 0)

    while l <= len_arr:
        i = 0
        j = l
        while j < len_arr:
            left = res[i][j-1]
            bottom = res[i+1][j]
            # understand this! Very important and subtle point
            # first is got by either
            # choosing starting element (i) and then choosing the best you can do with [i+1, j] (exclude the ith)
            # OR choosing the ending element (j) and then choosing the best you can do with [i, j-1] (exclude the jth)
            first = max([arr[i] + bottom[1], arr[j] + left[1]])
            if arr[i] + bottom[1] > arr[j] + left[1]:
                second = bottom[0]
            else:
                second = left[0]
            res[i][j] = (first, second)
            i += 1
            j += 1
        l += 1

    # return top right element - ie - 0 to entire length
    return res[0][len_arr - 1]

print(optimal_strategy([3, 9, 1, 2]))
print(optimal_strategy([5, 3, 7, 10]))
print(optimal_strategy([8, 15, 3, 7]))
print(optimal_strategy([1, 1]))
print(optimal_strategy([1]))
print(optimal_strategy([5, 4, 1, 3, 6, 2]))