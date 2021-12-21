# https://leetcode.com/problems/subsets-ii/submissions/
class Solution(object):
    def __init__(self):
        self.ss = []
        
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.helper(nums, [], 0)
        return self.ss
    
    def helper(self, nums, arr, start):
        # sort the potential subset 
        subset = sorted(arr)
        # only if this sorted subset is not in the subset list, then add
        if subset not in self.ss:
            self.ss.append(subset)
        for i in range(start, len(nums)):
            arr.append(nums[i])
            # what's very important here is that the third arg is i+1 and not start+1
            self.helper(nums, arr, i+1)
            arr.remove(nums[i])