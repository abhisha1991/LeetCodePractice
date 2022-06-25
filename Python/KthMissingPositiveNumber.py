# https://leetcode.com/problems/kth-missing-positive-number
# this is o(1) space but o(n) in time
class Solution:
    # [1,2,3], k = 2 --> result = 5 (special case - end of arr)
    # [3,4,5], k = 2 --> result = 2 (special case - front of arr)
    # [3,4,5,9], k = 3 --> result = 6 (general case)
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missed = 0
        for i in range(len(arr)):
            if i == 0:
                missed += arr[0] - 1
                # if missed interval from the start contains k
                # then return k, for example, arr [5,6,7] and k = 2
                # then we're missing [1,2,3,4] from the start and missed becomes arr[0] - 1 => 5-1 = 4
                if missed >= k:
                    return k
                
            else:
                # say arr was [3,4,5,9] 
                # and we're at element 2, ie, arr[2] = 5
                # for 2 consecutive numbers scenario
                # missed += offset, ie, missed += 5 - 4 - 1 ==> missed += 0
                
                # now if we move to element 3, ie, arr[3] = 9
                # then for 2 non-consecutive numbers scenario
                # missed += offset, ie, missed += 9 - 5 + 1 ==> missed += 3
                # this is correct because there are 3 numbers between 5 and 9, ie, [6,7,8]
                offset = arr[i] - arr[i-1] - 1
                missed += offset
                if missed >=k:
                    res = arr[i-1]
                    # revert back missed to what it was earlier and increment till we reach missed == k
                    missed -= offset
                    while missed < k:
                        res +=1
                        missed +=1
                    
                    # we kept incrementing until missed < k, now missed == k, so res is the kth number which was missing
                    return res
        
        # this is handling the case when arr = [1,2,3], k = 2, so the missing number is present toward the end of the arr
        res = arr[-1]
        while missed < k:
            res +=1
            missed +=1
        return res