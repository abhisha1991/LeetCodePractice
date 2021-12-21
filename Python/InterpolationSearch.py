# http://www.geeksforgeeks.org/interpolation-search/
# Similar to binary search, except we dont take the mid point to search


def interpolation_search(arr, start, end, x):
    if start <= end and arr[start] < arr[end]:
        pos = start + (x - arr[start]) * int(((end - start) / (arr[end] - arr[start])))
        if arr[pos] == x:
            return pos

        if arr[pos] > x:
            return interpolation_search(arr, start, pos, x)
        else:
            return interpolation_search(arr, pos + 1, end, x)

    return -1

print("Performing interpolation search")
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(interpolation_search(array, 0, len(array) - 1, 9))

print("Performing interpolation search")
array = [-1, 43, 56, 344, 4546, 46567, 99999]
print(interpolation_search(array, 0, len(array) - 1, 23))

print("Performing interpolation search")
array = [0, 0, 0, 0, 0]
print(interpolation_search(array, 0, len(array) - 1, 1))

print("Performing interpolation search")
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(interpolation_search(array, 0, len(array) - 1, 2))

print("Performing interpolation search")
array = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
print(interpolation_search(array, 0, len(array) - 1, 18))

print("Performing interpolation search")
array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
print(interpolation_search(array, 0, len(array) - 1, 1))