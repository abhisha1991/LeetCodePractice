# http://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/
import itertools
alist = list()

def countTriplets(a, summ):
    count = 0
    for subset in itertools.combinations(a, 3):
        if sum(subset) < summ:
            count = count + 1
            alist.append(subset)
    return count

print(countTriplets([1, 2, 3, 4, 5], 10))
print(alist)
alist.clear()

# https://discuss.leetcode.com/topic/23421/simple-and-easy-understanding-o-n-2-java-solution/2


def countTriplets2(a, summ):
    a = sorted(a)
    count = 0
    lena = len(a)
    for i in range(0, lena - 2):
        j = i + 1
        k = len(a) - 1
        while j < k:
            if a[i] + a[j] + a[k] < summ:
                alist.append([a[i], a[j], a[k]])
                k = k - 1 # This decision is arbitrary, you can choose to also do j += 1 and vice versa below
            else:
                # If the sum was bigger for this i, j, k, then it is guaranteed to be bigger for
                # i, j + 1, k and i, j + 2, k etc. - ie (k-j) times. Why? The array is sorted
                count = count + k - j
                j = j + 1

    return count

print(countTriplets2([1, 2, 3, 4, 5], 10))
print(countTriplets2([10, 11, 12, 13, 1, 2, 3, 4, 14, 15, 16, 17], 20))
print(alist)


# Theoretically this is O(n3) - DON'T USE THIS
def triplet_sum(arr, sumval):
    count = 0
    for i in range(len(arr)):
        j = i + 1
        k = len(arr) - 1
        if j == k:
            continue
        while j < k:
            # print("Combo is: ", arr[i], arr[j], arr[k])
            if sumval > arr[i] + arr[j] + arr[k]:
                count += 1
            j += 1
            if j == k:
                j = i + 1
                k -= 1

    return count

print("START")
print(triplet_sum([10, 11, 12, 13, 1, 2, 3, 4, 14, 15, 16, 17], 2000))


'''
-2 0 1 3

i = 0
j = 1
k = 1
count = 1
jk {1: 3, 2:3  }
'''

'''
t = int(input().strip())
for i in range(t):
    nx = [int(x) for x in input().strip().split(' ')]
    n = nx[0]
    x = nx[1]
    arr = [int(x) for x in input().strip().split(' ')]
    print(triplet_sum(arr, x))
'''