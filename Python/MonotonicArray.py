# https://leetcode.com/problems/monotonic-array/
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        n = len(nums)
        if n <= 1:
            return True
        
        i = 0
        j = 1
        monotonic = True
        
        # check for increasing
        while j < n:
            cur = nums[i]
            nxt = nums[j]
            
            if nxt >= cur:
                pass
            else:
                monotonic = False
                break
            i +=1
            j +=1
            
        if monotonic:
            return monotonic
        
        i = 0
        j = 1
        monotonic = True
        
        # check for decreasing
        while j < n:
            cur = nums[i]
            nxt = nums[j]
            
            if nxt <= cur:
                pass
            else:
                monotonic = False
                break
            i +=1
            j +=1
        
        return monotonic