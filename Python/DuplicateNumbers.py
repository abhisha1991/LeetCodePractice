# https://leetcode.com/problems/find-the-duplicate-number/description/
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://youtu.be/HuZJqRDOPo0?t=264
        for i in range(0, len(nums)):
            if nums[abs(nums[i])] >= 1:
                nums[abs(nums[i])] = -1 * nums[abs(nums[i])]
            else:
                return abs(nums[i])