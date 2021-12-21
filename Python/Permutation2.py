# https://leetcode.com/problems/permutations-ii/submissions/
# below solution is wrong, however, its closest to the answer. Try with input [2,2,3,3,3]
from collections import Counter
class Solution(object):
    def __init__(self):
        self.perms = []
        self.dic = dict()
        
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.dic = Counter(nums) # [2,2,3,3,3] --> for this it will return a dictionary = {2:2, 3:3}, ie, keys to number of occurrences
        self.helper(nums, [])
        return self.perms
    
    def helper(self, nums, arr):
        if len(arr) == len(nums) and arr not in self.perms and Counter(arr) == self.dic:
            self.perms.append(list(arr))
            return
            
        for i in range(0, len(nums)):
            # if the count of the current element in arr is less than the max number of occurrences of that element in nums
            # then we can still potentially add to arr and permute
            if self.dic[nums[i]] > arr.count(nums[i]):
                arr.append(nums[i])
                self.helper(nums, arr)
                arr.remove(nums[i])

# the below solution is correct, however, its fairly slow
# copied from geeks for geeks
class Solution(object):
    def __init__(self):
        self.perms = []
        
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = self.helper(nums)
        # permutations will contains duplicates, so the below dedupes them
        for p in permutations:
            if p not in self.perms:
                self.perms.append(p)
                
        return self.perms
    
    def helper(self, nums):
        if not nums:
            return  []
        
        if len(nums) == 1:
            return [nums]
        
        res = []
        for i in range(len(nums)):
            first = nums[i]
            rest = nums[:i] + nums[i+1:]
            for j in self.helper(rest):
                # j is going to be a list
                # so we are adding all permutations with first at the beginning
                res.append([first] + j)
                
        return res

#https://www.youtube.com/watch?time_continue=1&v=nYFd7VHKyWQ