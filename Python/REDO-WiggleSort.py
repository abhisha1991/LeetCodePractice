# https://www.geeksforgeeks.org/sort-array-wave-form-2/
# https://leetcode.com/problems/wiggle-sort-ii/discuss/


class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        print(nums)
        print(nums[::2])
        half = len(nums[::2]) - 1
        print(nums[half::-1])
        print(nums[:half:-1])
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]