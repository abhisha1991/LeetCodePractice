# http://www.geeksforgeeks.org/find-subarray-with-given-sum/
# not optimal, see below
def subarray_with_given_sum(summ, arr):
    if summ in arr:
        return summ

    if summ == sum(arr):
        return arr

    lenarr = len(arr)
    k = 2
    while k <= lenarr:
        j = 0
        for i in range(k, lenarr + 1):
            if j == lenarr:
                j = 0
            if sum(arr[j:i]) == summ:
                return arr[j:i]
            j += 1

        k += 1

    return None

subarray_with_given_sum(12, [1, 1, 1, 1, 10])
'''

t = int(input())
for i in range(t):
    ns = [int(x) for x in input().strip().split(' ')]
    arr = [int(x) for x in input().strip().split(' ')]
    print(subarray_with_given_sum(ns[1], arr))
'''


# Moving window concept - pretty smart - this is actually a O(n) solution, read G4G post on why!!!
# This only handles POSITIVE INTEGERS, SEE BELOW FOR NEGATIVE INTEGERS SOLUTION AS WELL

def subarr_with_given_sum(summ, arr):
    if summ in arr:
        return summ

    if sum(arr) == summ:
        return arr

    result = [arr[0]]
    k = 0
    flag = False
    for i in range(1, len(arr)):
        if sum(result) == summ:
            # return result
            ans = str(k+1) + ' ' + str(i)
            flag = True
            break

        while sum(result) > summ:
            result = result[1:]
            k += 1
            if sum(result) == summ:
                ans = str(k + 1) + ' ' + str(i)
                return ans

        result.append(arr[i])

    if flag:
        return ans

    while sum(result) > summ:
        result = result[1:]
        k += 1

    if sum(result) == summ:
        # return result
        ans = str(k+1) + ' ' + str(len(arr))
        return ans

    return -1

print("Performing subarr_with_given_sum - only positive numbers")
print(subarr_with_given_sum(12, [1, 2, 3, 7, 5]))
print(subarr_with_given_sum(528, [26, 144, 125, 24, 173, 62, 182, 4, 33, 106, 194, 126, 32, 93,
                              143, 23, 87, 65, 101, 188, 161, 14, 175, 71, 171, 36, 34,
                              112, 161, 97, 68, 86, 151, 141, 95, 96, 25, 20, 126, 177,
                              95, 59, 103, 172, 67, 79, 194, 52, 85, 19, 65, 120, 153, 1, 88, 61,
                              127, 11, 158, 171, 116, 177, 28, 44, 159, 165, 110, 83, 87, 166, 88,
                              178, 75, 26, 28, 30, 129, 24, 121, 103, 163, 124, 197,
                              138, 62, 196, 126, 65, 61, 3, 117, 31, 127, 12, 172, 12, 148, 154, 121, 191]))

print(subarr_with_given_sum(16, [1, 1, 1, 1, 11]))
print(subarr_with_given_sum(468, [135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92,
                                  196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127,
                                  172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]))


# http://www.geeksforgeeks.org/find-subarray-with-given-sum-in-array-of-integers/
# EXPLANATION IN THE STACK OVERFLOW LINK BELOW - REDO THIS QUESTION IF POSSIBLE
# https://stackoverflow.com/questions/39322019/using-a-map-to-find-subarray-with-given-sum-with-negative-numbers


def subarr_with_given_sum_neg_allowed(summ, arr):
    dic = dict()
    curr_sum = 0
    for i in range(0, len(arr)):
        curr_sum += arr[i]

        if curr_sum == summ:
            return arr[0:i+1]

        # this is curr_sum - summ, not the other way around. why? See stack overflow
        if curr_sum - summ in dic.keys():
            start = dic[curr_sum - summ] + 1
            return arr[start:i+1]

        # this is curr_sum - summ, not the other way around. why? See stack overflow
        dic[curr_sum] = i

    return None

print("Performing subarr_with_given_sum - with negative numbers allowed")
print(subarr_with_given_sum_neg_allowed(-10, [10, 2, -2, -20, 10]))
print(subarr_with_given_sum_neg_allowed(0, [10, 2, -2, -20, 10]))
