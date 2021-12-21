# http://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
maxi = -999


def get_largest(arr, low, high):
    global maxi
    if low <= high:
        mid = int((low + high) / 2)
        if mid >= len(arr):
            return maxi

        if arr[mid] > maxi:
            maxi = arr[mid]
        ele = max(get_largest(arr, low, mid - 1), get_largest(arr, mid + 1, high))
        if ele > maxi:
            maxi = ele
        return maxi

    else:
        return maxi


def binary_search(ele, arr, low, high):
    mid = int((low + high) / 2)
    if mid < low or mid > high:
        return -1
    if arr[mid] == ele:
        return mid
    if low <= high:
        if ele > arr[mid]:
            return binary_search(ele, arr, mid + 1, high)
        else:
            return binary_search(ele, arr, low, mid - 1)
    return -1


t = int(input())
for i in range(t):
    nx = [int(x) for x in input().strip().split(' ')]
    eles = [int(x) for x in input().strip().split(' ')]
    maxi = -999
    large = get_largest(eles, 0, nx[0])
    idx = eles.index(large)
    y = binary_search(nx[1], eles, 0, idx)
    z = binary_search(nx[1], list(reversed(eles[idx+1:])), 0, len(list(reversed(eles[idx+1:]))) - 1)
    if z is not -1:
        z = (nx[0] - 1 - z)

    if y == -1 and z == -1:
        print("OOPS! NOT FOUND")
    else:
        if y != -1:
            print(y)
        else:
            print(z)
