# easy solution
# https://www.youtube.com/watch?v=bGC2fNALbNU&t=586s
# https://leetcode.com/problems/subsets/discuss/27288

def subset(given_arr):
    ss = [None] * len(given_arr)
    helper(given_arr, ss, 0)


def helper(given_arr, ss, i):
    if i == len(given_arr):
        print(ss)
    else:
        # dont include the ith element at given_arr and call helper
        ss[i] = None
        helper(given_arr, ss, i + 1)
        # include the ith element at given_arr and call helper
        ss[i] = given_arr[i]
        helper(given_arr, ss, i + 1)


subset([1, 2])

subset([1, 2, 3, 4, 5])
