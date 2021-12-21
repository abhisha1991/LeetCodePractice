# https://www.youtube.com/watch?v=kekmCQXYwQ0
# Kadanes algo
def max_sum_subarray(arr):
    sum_ending_here = 0
    max_so_far = arr[0]
    start = 0
    end = 0
    s = 0
    for i in range(len(arr)):
        sum_ending_here = sum_ending_here + arr[i]
        if sum_ending_here > max_so_far:
            max_so_far = sum_ending_here
            start = s
            end = i
        if sum_ending_here <= 0:
            sum_ending_here = 0
            s = i + 1

    return arr[start: end + 1]

print(max_sum_subarray([1, 0, -1, -1, -1, 5, 6, -7, 9, 9, 10, -1, -2]))
print(max_sum_subarray([1, 2, 3, 4, 5]))
print(max_sum_subarray([1]))
print(max_sum_subarray([-1, 2, -3, 4, -5]))
print(max_sum_subarray([-1, -2, -3, -4, -5]))
print(max_sum_subarray([-1, -2, -3, -4, 6, 7, 9]))