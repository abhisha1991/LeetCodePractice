# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # mnq will hold numbers in strictly increasing order, for example, [1,3,6,9]
        # mxq will hold numbers in strictly decreasing order, for example, [9,6,3,1]
        mnq, mxq = deque(), deque()
        
        # the idea is that we want to track the max and min of any sub array in question
        # why max and min? because if for a given subarray, abs(max - min) is <= limit, then any other pair of numbers
        # in the sub array will also satisfy the condition of abs(num1 - num2) <= limit
        
        # the idea is to use sliding window and two monotonic queues to keep track of the window max and window min 
        # so keep 2 pointers left and right, initially both at 0
        # keep incrementing right as long as condition of abs(max - min) is <= limit is satisfied
        # when it stops being satisfied, increment left to shrink the window from the left side
        
        l = 0 
        r = 0
        res = 0
        
        # our right pointer is something like the "current" index which is always incremented, no matter what
        while r < len(nums):
            # check if the number we're inserting (nums[r]) is less than "equal to" (strictly increasing criteria)
            # the last element of mnq - last element of mnq will contain idx of largest value of nums
            # so if the number we're appending is smaller than (or equal to) largest num in mnq, 
            # we cannot insert nums[r] in last pos since the strictly increasing criteria violates, 
            # so we need to pop till nums[r] becomes the largest in mnq and its safe to append 'r' in the last pos
            while mnq and nums[r] <= nums[mnq[-1]]:
                mnq.pop()
            
            # same logic with mxq when inserting nums[r]
            while mxq and nums[r] >= nums[mxq[-1]]:
                mxq.pop()
            
            # note that we're appending the index and not the actual value in the queues
            # the criteria for insertion - shown above in the while loops is to maintain the strictly increasing/decreasing
            # nature of the 2 queues
            mnq.append(r)
            mxq.append(r)
            
            # if the max - min becomes greater than limit, we need to shrink our left side
            # this algo may not seem o(n) but it is because for each index, we add it and then remove it from queue
            while nums[mxq[0]] - nums[mnq[0]] > limit:
                # increment left window pointer
                l += 1
                
                # we need to throw out any invalid window indices from the queues
                # if our left pointer of window has moved further "right" than what is there in the 
                # front of any of the queues, then pop
                if l > mnq[0]:
                    mnq.popleft()
                
                if l > mxq[0]:
                    mxq.popleft()
            
            # calculate size of window
            # remember to always add +1 in window calculation
            res = max(res, r - l + 1)
            # always increment right no matter what, since right is acting like our "current" index
            r += 1
                
        return res