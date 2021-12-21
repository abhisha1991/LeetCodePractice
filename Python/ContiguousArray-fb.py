# https://leetcode.com/problems/contiguous-array/
# below solution is not efficient
class Solution2(object):
    def __init__(self):
        self.n = 0
        self.maxi = 0
        
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = len(nums) - 1
        
        if j <= 0:
            return 0
        
        self.n = j + 1
        # replace all 0s with -1
        nums = [x-1 if x ==0 else x for x in nums]
        # the idea is that we need to now find the largest subarray with sum 0, as that will have equal number of 1s and -1s
        self.helper(nums, 0, j)
        return self.maxi
    
    def helper(self, nums, i, j):
        if j <= i or i < 0 or j >= self.n:
            return
        
        if sum(nums[i:j+1]) == 0:
            res = j-i+1
            if self.maxi < res:
                self.maxi = res
        
        # we incremenet i and keep j same and evaluate the outcome
        self.helper(nums, i+1, j)
        # we decrement j and keep i same and evaluate the outcome
        self.helper(nums, i, j-1)

# read https://leetcode.com/problems/contiguous-array/solution/
class Solution(object):
    def __init__(self):
        self.n = 0
        self.maxi = 0
        self.dic = {0:0}
        
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for idx, num in enumerate(nums, 1):
            if num == 0:
                count -=1
            else:
                count +=1
        
            if count not in self.dic:
                self.dic[count] = idx
            else:
                self.maxi = max(self.maxi, idx - self.dic[count])
        
        return self.maxi
        