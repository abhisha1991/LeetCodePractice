# http://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
import itertools


# Correct solution - takes too long!! Don't use this!
def min_sum_partition2(arr):
    partition1 = []
    partition2 = []
    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return arr[0]

    if len(arr) == 2:
        return abs(arr[0] - arr[1])

    mini = 100000
    all_sum = sum(arr)
    for i in range(len(arr)):
        for j in itertools.combinations(arr, i):
            temp_diff = abs(sum(j) - (all_sum - sum(j)))
            if temp_diff < mini:
                mini = temp_diff
                partition1 = j
                if mini == 0:
                    print(list(partition1))
                    partition2 = [x for x in arr if x not in partition1]
                    print(partition2)
                    print(mini)
                    return mini

    print(list(partition1))
    partition2 = [x for x in arr if x not in partition1]
    print(partition2)
    print(mini)
    return mini

min_sum_partition2([-1, 2, 3, 4, 5, 6, 7, 8, 9, -15, 2, 3, 16, -1, 34, 465, 5])

# Correct solution!!

def min_sum_partition(arr):
    lenarr = len(arr)
    sumarr = sum(arr)
    msp = []
    for i in range(lenarr):
        temp = [None] * (sumarr + 1)
        msp.append(temp)
    '''
        0 1 2 3 4 5 6 7 8 9 10
      1 T T F F F F F F F F F 
      2 T T T T F F F F F F F
      3 T T T T T T T F F F F
      4 T T T T T T T T T T T 
    '''
    for i in range(lenarr):
        for j in range(sumarr + 1):
            if j == 0:
                msp[i][j] = True
                continue
            if i == 0:
                if arr[i] == j:
                    msp[i][j] = True
                else:
                    msp[i][j] = False
                continue
            if arr[i] > j:
                msp[i][j] = msp[i-1][j]
            else:
                msp[i][j] = msp[i-1][j] or msp[i-1][j - arr[i]]

    # Basically its the same problem of finding whether a subset has a given sum
    # Here is where things change - for the last row - ie - for the entire set
    # We go through each sum and we try to find the sum 'j' that is capped at sumarr/2
    # such that, we have a subset that can be added up to 'j' and its difference with summarr is least
    j = 0
    ans = 0
    while sumarr - j * 2 >= 0:
        if msp[lenarr - 1][j]:
            ans = sumarr - j * 2
        j += 1

    return ans

min_sum_partition([37, 28, 16, 44, 36, 37, 43, 50, 22, 13, 28, 41, 10, 14, 27, 41, 27, 23, 37, 12, 19, 18, 30, 33, 31
                      ,13, 24, 18, 36, 30, 3, 23, 9, 20])
'''
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    arr = [int(x) for x in input().strip().split(' ')]
    print(min_sum_partition(arr))
'''

