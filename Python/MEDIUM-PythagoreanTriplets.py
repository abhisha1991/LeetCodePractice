import math

# http://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/

# Important to make i start from the end!!
# Similar to count triplets problem but different as we sort and then start from the end
# k is starting at i-1, j starts at 0

# special attention to the fact that we have i going from right to left and stopping at index 1
# note if k is negative, then we will break out of while loop anyway

def pythagorean_triplet(arr):
    arr = sorted(arr)
    for i in range(len(arr) - 1, 1, -1):
        k = i - 1
        j = 0

        while j < k:
            lhs = (arr[k] * arr[k]) + (arr[j] * arr[j])
            rhs = arr[i] * arr[i]
            if lhs == rhs:
                return "Yes"
            if rhs > lhs:
                j += 1
            elif lhs > rhs:
                k -= 1
    return "No"

print(pythagorean_triplet([42,12,54,69,48,45,63,58,38,60,24,42,30,79,17,36,91,43,89,7,41,43,65,49,47,6,91,30,71,51,7,2,94,49,30,24,85,55,57,41,67,77,32,9,45,40,27,24,38,39,19,83,30,42,34,16,40,59,5,31,78]))
# 42,12,54,69,48,45,63,58,38,60,24,42,30,79,17,36,91,43,89,7,41,43,65,49,47,6,91,30,71,51,7,2,94,49,30,24,85,55,57,41,67,77,32,9,45,40,27,24,38,39,19,83,30,42,34,16,40,59,5,31,78
# 42 12 54 69 48 45 63 58 38 60 24 42 30 79 17 36 91 43 89 7 41 43 65 49 47 6 91 30 71 51 7 2 94 49 30 24 85 55 57 41 67 77 32 9 45 40 27 24 38 39 19 83 30 42 34 16 40 59 5 31 78
'''
t = int(input())
for i in range(t):
    n = int(input())
    ip = [int(x) for x in input().strip().split(' ')]
    print(pythagorean_triplet(ip))
'''