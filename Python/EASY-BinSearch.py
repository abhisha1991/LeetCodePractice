# http://www.geeksforgeeks.org/binary-search/
import time


def linear_search(arr, search_ele):
    tick = time.time()
    for i in arr:
        if i == search_ele:
            tock = time.time()
            print("Linear search: ", tock - tick)
            return True

    tock = time.time()
    print("Linear search: ", tock - tick)
    return False


tick = time.time()

# Lesson learnt! - always include return statements [even for binary_search call],
# else what you return as arr[mid] == search_ele will never be actually returned from binary_search


def binary_search(arr, low, high, search_ele):
    lo = low
    print("low: ", lo)
    mid = int((high + low) / 2)
    print("mid: ", mid)
    hi = high
    print("high: ", hi)
    if arr[mid] == search_ele:
        tock = time.time()
        # print("Bin search: ", tock - tick)
        return True
    if lo <= hi:
        if search_ele > arr[mid]:
            if binary_search(arr, mid + 1, hi, search_ele):
                return True
        else:
            if binary_search(arr, lo, mid - 1, search_ele):
                return True

    tock = time.time()
    # print("Bin search: ", tock - tick)
    return False

x = [1, 3, 4, 7, 8, 9, 10, 11, 14, 16, 20, 30, 32, 40]
print(binary_search(x, 0, len(x) - 1, 3))