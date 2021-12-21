# section 5.13 from EPI book
# the motivation of this problem comes from network packet selection for inspection.
# where we need to select k packets from a stream of incoming packets
import random
def sampleOnlineData(arr, k):
    # select first k elements out of arr
    # why are we making a new list?
    # because otherwise we will be pointing a ref to arr, which is not what we want
    res = list(arr[:k])

    nums_seen = k
    for x in arr:
        nums_seen +=1
        # generate a number between [0, nums_seen-1]
        # if this number is in [0,k-1], we replace that number with x in the res
        # remember, randint is inclusive of range LHS and RHS
        idx_to_replace = random.randint(0, nums_seen-1)
        if idx_to_replace < k:
            res[idx_to_replace] = x
    return res

for i in range(10):
    print(sampleOnlineData([1,2,3,4,5,6,7,8,9,10],3))
