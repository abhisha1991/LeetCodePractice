# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
def array_left_rotation(a, n, k):
    if k >= n:
        # number of rotations is more than length
        k = k % n
    partition = a[0:k]
    if len(partition) is 0:
        return a
    a = a[k:]
    a.extend(partition)
    return a

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')
