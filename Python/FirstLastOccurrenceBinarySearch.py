# https://www.youtube.com/watch?v=OE7wUUpJw6I&list=PL2_aWCzGMAwLPEZrZIcNEq9ukGWPfLT4A
# fnd the first and last occurrences of given target in a sorted array using binsearch
def firstbin(arr, target):
    result = -1
    low = 0
    high = len(arr)-1
    
    while low <= high:
        mid = int((low+high)/2)
        if arr[mid] == target:
            result = mid
            high = mid - 1
        elif arr[mid] > target:
            high = mid - 1
        else: # arr[mid] < target
            low = mid + 1
    return "first index is {0} where we find element {1}".format(result, target)

print(firstbin([1,2,3,3,3,3,4,5,6,7], 3))

def lastbin(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1
    while low <= high:
        mid = int((low+high)/2)
        if arr[mid] == target:
            result = mid
            low = mid+1
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return "last index is {0} where we find element {1}".format(result, target)

print(lastbin([1,2,3,3,3,3,4,5,6,7], 3))

'''
One interesting application of this problem is that we can find how many counts of a target number are in an array
For example, we can find the number of times 3 occurs in the above array in log n time - which is better than o(N) time
ans = print(lastbin([1,2,3,3,3,3,4,5,6,7], 3)) - print(firstbin([1,2,3,3,3,3,4,5,6,7], 3)) + 1
so we're basically doing, ans = lastindex - firstindex + 1 (5-2+1 = 4). There are 4 counts of number 3

'''