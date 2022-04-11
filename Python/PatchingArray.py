# https://leetcode.com/problems/patching-array/
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # i is index of nums
        i = 0
        
        # just rename n as target, more intuitive
        target = n
        
        # upto is the sum we can create so far with our existing elements in nums
        upto = 0
        
        # missing contains the numbers that we want to add/patch
        # to extend our range
        missing = []
        while upto < target:
            if i < len(nums) and nums[i] <= upto+1:
                upto += nums[i]
                i+=1
            else:
                miss = upto+1
                missing.append(miss)
                upto += miss
                print(f"new range we can cover if we patch with missing numbers: {upto}")

        print(f"new range we can cover if we patch with missing numbers: {upto}")
        print(f"missing is {missing}")
        return len(missing)