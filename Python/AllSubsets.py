# https://leetcode.com/problems/subsets/
# this is a helpful post for solving any backtracking problem class
# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
class Solution(object):
    def __init__(self):
        self.ss = []
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.helper(nums, 0, [])
        return self.ss
    
    def helper(self, nums, start, tmp):
        self.ss.append(list(tmp))
        for j in range(start, len(nums)):
            tmp.append(nums[j])
            self.helper(nums, j + 1, tmp)
            tmp.remove(nums[j])