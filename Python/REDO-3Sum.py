# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        
        # there must be 3 elements in a triplet
        if n < 3:
            return []
        
        # create a set for non duplicate
        output = set()
        for i in range(n):
            # if curr value is > 0 in sorted array, all values after it will be positive, so no point looking  
            if nums[i] > 0:
                continue
            
            j = i+1
            k = n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    output.add((nums[i], nums[j], nums[k]))
                    j +=1
                    k -=1
                # sum is too high in sorted array, decrement from kth pos
                elif s > 0:
                    k -=1
                # sum is too low in sorted array, increment from jth pos
                elif s < 0:
                    j +=1
                    
        # convert result back to list format
        return [list(i) for i in output]