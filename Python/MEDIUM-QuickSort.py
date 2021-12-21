# http://www.geeksforgeeks.org/quick-sort/
# https://www.youtube.com/watch?v=COk73cpQbFQ&t=944s - look at this for basic quick sort explain
# https://www.youtube.com/watch?v=3Bbm3Prd5Fo
# randomized quick sort [avoids worst case O(n2) - reduces it to O(n log(n)) always] - look at 2nd video above
# Also look at the time/space complexity analysis derivation of quick sort in the 2nd video


def quick_sort(arr, start, end):
    if start < end:
        pIndex = partition(arr, start, end)
        # partition is in correct place, so look at left and right of partition
        quick_sort(arr, start, pIndex - 1)
        quick_sort(arr, pIndex + 1, end)


def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start
    i = start
    while i <= end - 1:
        if arr[i] < pivot:
            arr = swap(arr, i, pIndex)
            pIndex += 1
        i += 1

    arr = swap(arr, end, pIndex)
    return pIndex


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


# Test for partition
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = partition(x, 0, len(x)-1)
print(y)
print(x)

t = int(input())
for i in range(t):
    n = int(input())
    nums = [int(x) for x in input().strip().split(' ')]
    quick_sort(nums, 0, len(nums) - 1)
    ans = ''
    for i in nums:
        ans += str(i) + ' '
    print(ans)