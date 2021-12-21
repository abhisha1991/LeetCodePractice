# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) is 0:
            return -1

        j = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                j = i
                break
        x = self.binsearch(nums, 0, j, target)
        y = self.binsearch(nums, j + 1, len(nums) - 1, target)
        if x is -1 and y is -1:
            return -1
        elif x != -1:
            return x
        return y

    def binsearch(self, nums, lo, hi, target):
        if lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.binsearch(nums, lo, mid - 1, target)
            else:
                return self.binsearch(nums, mid + 1, hi, target)
        return -1