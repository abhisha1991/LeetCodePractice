# http://www.geeksforgeeks.org/given-sorted-array-number-x-find-pair-array-whose-sum-closest-x/
import sys


def closest_sum(arr, summ):
    i = 0
    j = len(arr) - 1
    prev_sum = sys.maxsize
    while i < j:
        print('arr[i] and arr[j]: ', arr[i], arr[j])
        if abs(arr[i] + arr[j] - summ) <= abs(prev_sum - summ):
            prev_sum = arr[i] + arr[j]
            print('The pair contributing to this new closest sum is ', i, j)
        if arr[i] + arr[j] < summ:
            i += 1
        else:
            j -= 1
    print(prev_sum)
    return prev_sum

print("Getting closest sum")
x = [10, 22, 28, 29, 35, 40, 54]
closest_sum(x, 54)
# Observe in the output - we had (22 + 35 = 57 and 57 - 54 = 3) - but this is not the 57 displayed
# Also we had then (22 + 29 = 51 and 51 - 54 = 3) - but 51 was not displayed
# Then we finally had (28 + 29 = 57 and 57 - 54 = 3) - this was the 57 that was displayed!
print("Getting closest sum")
x = [10, 22, 29, 29, 35, 40, 54]
closest_sum(x, 54)