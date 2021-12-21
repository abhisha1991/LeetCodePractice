# https://codefights.com/interview/3gY7eyeRMZeARKmyQ
# look at the other file - subset sum problem
def subsetSum(arr):
    sum_of_arr = sum(arr)
    # if sum is odd, then you cant divide into 2 equal arrays [assuming arrays are int]
    if (sum_of_arr % 2 != 0):
        return False

    arr = list(sorted(arr))
    length = len(arr)
    # if the largest element in the array matches target
    if (arr[length - 1] == sum_of_arr / 2):
        return True

    # if any element is greater than target, then you cant divide array into 2 subsets
    if (any(x > (sum_of_arr / 2) for x in arr)):
        return False

    target = sum_of_arr / 2
    # initialize 2d array of False values
    rows = int(length)
    cols = int(target + 1)
    m = [[False for x in range(0, cols)] for y in range(0, rows)]

    # mark the first column as true as you can return empty subset
    for i in range(0, rows):
        m[i][0] = True

    for x in range(0, rows):
        for y in range(0, cols):
            k = x - 1
            if k is -1:
                k = 0
            # TODO: The second condition after 'or' doesnt make sense still
            # y refers to index as well as temp target sum, so we subtract a[x] from it which gives us
            # the column position in the above row to look for a true/false value
            m[x][y] = m[k][y] or m[k][y - arr[x]]

    # return last element of the matrix as that contains the bool for the target
    return m[rows - 1][cols - 1]


# subsetSum([3, 5, 16, 8])
# subsetSum([5, 7, 1])
# subsetSum([858, 395, 29, 237, 235, 793, 818, 428, 143, 11, 928, 529, 776, 404, 443, 763, 613, 538, 606, 840, 904, 818])
subsetSum([87, 56, 43, 91, 27, 65, 59, 36, 32, 51, 37, 28, 75, 7, 74])
