# http://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
maxi = -999


def get_largest(arr, low, high):
    global maxi
    if low <= high:
        mid = int((low + high) / 2)

        if arr[mid] > maxi:
            maxi = arr[mid]

        ele = max(get_largest(arr, low, mid - 1), get_largest(arr, mid + 1, high))

        if ele > maxi:
            maxi = ele

        return maxi

    else:
        return maxi

'''
x = [98, 2, 101, 8, -6, 4, 3, 10, 34, 87]
large = get_largest(x, 0, len(x) - 1)
print(large)
print(x.index(large))
'''


def search_ele(element, arr, low, high):
    mid = int((low+high)/2)
    if arr[mid] == element:
        return True
    if low <= high:
        if element > arr[mid]:
            return search_ele(element, arr, mid + 1, high)
        else:
            return search_ele(element, arr, low, mid - 1)

    return False


x = [4, 5, 6, 9, 1, 2, 3]
large = get_largest(x, 0, len(x) - 1)
idx = x.index(large)
search = 3
left = search_ele(search, x, 0, idx)
right = search_ele(search, x, idx + 1, len(x) - 1)
print("Left is ", left)
print("Right is ", right)
print(left or right)
