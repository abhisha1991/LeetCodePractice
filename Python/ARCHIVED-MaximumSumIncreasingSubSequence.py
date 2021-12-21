# https://www.youtube.com/watch?v=99ssGWhLPUE

from copy import deepcopy


def max_sum_inc_sub_seq(arr):
    n = len(arr)
    # https://stackoverflow.com/questions/17873384/deep-copy-a-list-in-python
    max_sum = deepcopy(arr)
    pos = []
    for x in range(0, len(arr)):
        pos.append(x)
    i = 1
    j = 0
    maxi = -1
    pos_max = -1
    while i < n:
        if j == i:
            j = 0
            i += 1
            if i == n:
                break

        if arr[j] < arr[i]:
            old_sum = max_sum[i]
            max_sum[i] = max(max_sum[i], max_sum[j] + arr[i])
            if maxi < max_sum[i]:
                maxi = max_sum[i]
                pos_max = i
            if max_sum[i] > old_sum:
                pos[i] = j

        j += 1

    if pos_max == -1:
        maxi = max(max_sum)
        pos_max = max_sum.index(maxi)

    print("Max sum is", maxi)
    print("Pos array is ", pos)
    print("The array elements contributing to the max sum are")
    summ = arr[pos_max]
    print(arr[pos_max])
    while summ != maxi:
        pos_max = pos[pos_max]
        print(arr[pos_max])
        summ += arr[pos_max]

max_sum_inc_sub_seq([4, 6, 1, 3, 8, 4, 6])
max_sum_inc_sub_seq([1, 1, 1])
max_sum_inc_sub_seq([1, 2, 3, 4, 5, 6, 7, 8])
max_sum_inc_sub_seq([-1, 2, 3, 4, 5, 6, 7, 8])
