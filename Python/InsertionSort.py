# http://www.geeksforgeeks.org/insertion-sort/
def insertion_sort(arr):
    if len(arr) == 1:
        return arr
    i = 0
    j = 1
    while j < len(arr):
        aj = arr[j]
        while arr[i] > aj:
            arr[i+1] = arr[i]
            i -= 1
            if i < 0:
                arr[i+1] = aj
                break
        if i >= 0 and arr[i] <= aj:
            arr[i+1] = aj
        i = j
        j += 1
    return arr


x = [7, 6, 4, 5, 3, 1, 2, 0, -1, 123, 12, 34, 1, 43, 2]
print(insertion_sort(x))
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(insertion_sort(x))
x = [9]
print(insertion_sort(x))
x = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(insertion_sort(x))
x = [-9, -8, -7, -6, -5, -4, -3, -2, -1]
print(insertion_sort(x))
x = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
print(insertion_sort(x))
x = [0, 0, 0, 0]
print(insertion_sort(x))