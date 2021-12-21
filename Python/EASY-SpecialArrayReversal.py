# http://www.geeksforgeeks.org/reverse-an-array-without-affecting-special-characters/
def reverse_str(arr):
    i = 0
    j = len(arr) - 1
    arr = list(arr)
    while (i <= j):
        if is_char(arr, i) and is_char(arr, j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
            continue

        if is_char(arr, i) == False:
            i += 1

        if is_char(arr, j) == False:
            j -= 1

    return ''.join(arr)


def is_char(array, pos):
    return (array[pos] >= 'a' and array[pos] <= 'z') or (array[pos] >= 'A' and array[pos] <= 'Z')


t = int(input().strip())
for i in range(t):
    print(reverse_str(input().strip()))