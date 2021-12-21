# section 5.12 of the EPI book
# given an array, return a subset of k elements which are randomly returned
import random
def sampleRandom(arr, k):
    for i in range(k):
        # generate a random number between i and length of arr
        # randint generates number inclusive of the edges, hence, we cannot give len(arr) as RHS boundary
        r = random.randint(i, len(arr)-1)
        # then swap ith element with this random number
        tmp = arr[r]
        arr[r] = arr[i]
        arr[i] = tmp

    # return first k elements at the end (as you only want a subset)
    return arr[:k]

# driver program
for i in range(10):
    print(sampleRandom([1,2,3,4,5], 3))