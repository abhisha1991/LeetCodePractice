# http://www.geeksforgeeks.org/find-smallest-value-represented-sum-subset-given-array/
#### DIDNT UNDERSTAND ABOVE SOLUTION - REDO ####
import itertools

######## VERY IMPORTANT SET RELATED INFO #########
print("Begin lesson on sets - not part of the question")
setx = set()
# cant do update() on numbers
setx.add(100)
print(setx)
# cant do add() on lists
setx.update([2,3,1])
print(setx)
# searching within a set
if 1 in setx:
    print("YES")

# removes a specific element from set
setx.discard(100)
print(setx)

# removes first element from set
y = setx.pop()
print(y)

print(setx)

print("End lesson on sets - not part of the question")

# Correct, however, the solution is slow - expected is O(n)


def smallest_number_subset(arr):
    lenarr = len(arr)
    setx = set()
    # if the array begins with something other than 1, then 1 is the smallest sum
    if arr[0] != 1:
        return 1

    for i in range(1, lenarr + 1):
        for x in itertools.combinations(arr, i):
            sumx = sum(x)
            setx.add(sumx)

    prev = setx.pop()
    while len(setx) > 0:
        curr = setx.pop()
        if curr - prev > 1:
            return prev + 1
        prev = curr

    if len(setx) == 0:
        curr = curr + 1

    return curr


print(smallest_number_subset([1, 3, 6, 10, 11]))
print(smallest_number_subset([1, 1, 1, 1]))
print(smallest_number_subset([1, 1, 3, 4]))
print(smallest_number_subset([1, 2, 5, 10, 20, 40]))
print(smallest_number_subset([1, 2, 3, 4, 5, 6]))
print(smallest_number_subset([2, 5, 6, 10, 20]))

'''
t = int(input().strip())
for i in range(t):
    n = int(input())
    x = [int(y) for y in input().strip().split(' ')]
    print(smallest_number_subset(x))
'''