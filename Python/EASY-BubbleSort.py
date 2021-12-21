# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
import time

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

total_swap = 0
for i in range(0,len(a)):
    swap = 0
    for j in range(0, len(a) - 1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            swap += 1
    # if no 2 elements were swapped by the inner loop, we already have a sorted array
    if swap == 0:
        break
    total_swap += swap

print("Array is sorted in", total_swap, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[len(a) - 1])


# http://www.geeksforgeeks.org/bubble-sort/
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        j = i + 1
        while j < len(arr):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            j += 1
    return arr

tick = time.time()
print(bubble_sort([5, 45, 34, 1, 45, 55, 5, 76, 1, 0, 12, 34, 6, 67, 67, 8, 9, 1, 2, 7, 6, 5, 4, 2, 3, 1]))
tock = time.time()
print(tock - tick)


'''
t = int(input())
for i in range(t):
    n = int(input())
    nums = [int(x) for x in input().strip().split(' ')]
    arr = bubble_sort(nums)
    print(arr)
'''