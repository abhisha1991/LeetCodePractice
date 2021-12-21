import copy
# http://www.geeksforgeeks.org/length-largest-subarray-contiguous-elements-set-1/
# This is O(n2), which is not ideal


def longest_continuous_subset(arr):
    arr = sorted(arr)
    # print(arr)
    maxi = 0
    for i in range(len(arr)):
        j = i + 1
        k = i
        result = []
        while j < len(arr):
            if arr[k] == arr[j] - 1:
                result.append(arr[k])
            else:
                break
            j += 1
            k += 1
        result.append(arr[k])
        # print(result)
        if len(result) > maxi:
            maxi = len(result)
            # print("maxi is:", maxi)
            print(result)

    print("Final maxi is: ", maxi)
    return maxi


# longest_continuous_subset([1, 2, 4, 5, 6])
longest_continuous_subset([1, 98, 99, 100, 2, 56, 80, 4, 5, 6, 7, 8, 96, 97])

# optimal solution below, O(nLog(n)) - why? because of the sort
# https://www.youtube.com/watch?time_continue=377&v=O7gf0a4c_5c (Geeks for geeks)
# They do it in O(n2), the difference is that we use an extra space (deep copy array), they dont


def longest_contiguous_subset2(arr):
    arr2 = copy.deepcopy(arr)
    arr2.sort()
    maxi = -99
    count = 1
    for i in range(len(arr2) - 1):
        if arr2[i] == arr2[i+1] - 1:
            count += 1
        else:
            if count > maxi:
                maxi = count
                count = 1

    if count > maxi:
        maxi = count

    print(maxi)
    return maxi


longest_contiguous_subset2([1, 98, 99, 100, 2, 56, 80, 4, 5, 6, 7, 8, 96, 97])
longest_contiguous_subset2([1, 56, 58, 57, 90, 92, 94, 93, 91, 45])
longest_contiguous_subset2([14, 12, 11, 20])