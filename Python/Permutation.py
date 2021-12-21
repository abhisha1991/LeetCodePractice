# https://leetcode.com/problems/permutations/
class Solution(object):
    def __init__(self):
        self.perms = []
        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.helper(nums, [])
        return self.perms
    
    def helper(self, nums, arr):
        if len(set(arr)) == len(nums):
            self.perms.append(list(arr))
            return
        
        # here, observe that we are considering from 0 to len(nums) every time (when looping)
        # in subsets / combination sum type problems, we generally do start --> len(nums)
        # why do we do from 0 here? because we want to consider backward elements as well
        # example, in [1,2,3]. we strt with [1] and our search space is only [2,3] in subset problem
        # here, if we start with [3], we want to consider [1,2] in our search space as well
        for j in range(0, len(nums)):
            # the if line ensure that we dont consider any duplicate numbers in arr
            if nums[j] not in arr:
                arr.append(nums[j])
                self.helper(nums, arr)
                arr.remove(nums[j])

        