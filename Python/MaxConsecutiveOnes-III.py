# https://leetcode.com/problems/max-consecutive-ones-iii
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        mx = 0
        
        # sliding window
        for right, n in enumerate(nums):
            # we're using up our available k by flipping a 0 to 1
            if n == 0:
                k -=1
                
            if k < 0:
                # now we can't flip any more 0s to 1
                # so now we have to start shrinking our window from the left
                # if current left part of the arr is a zero, then we can increment k 
                # because we are getting rid off a zero in the window
                if nums[left] == 0:
                    k+=1
                
                # incrementing left implies we are shrinking the window
                left +=1
                
            mx = max(mx, right - left + 1)
                
        return mx