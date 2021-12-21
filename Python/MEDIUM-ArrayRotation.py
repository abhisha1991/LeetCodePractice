# https://leetcode.com/problems/rotate-array/discuss/54250
# read the comments!
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        '''
        1 2 3 4 5 6 7
        k = 3
        logic:
        reverse the whole array
        7 6 5 4 3 2 1
        take 1st k elements and reverse
        5 6 7 4 3 2 1
        take n-k elements and reverse
        5 6 7 1 2 3 4

        '''
        if k >= len(nums):
            k = k % len(nums)

        nums = self.reverse(nums, 0, len(nums) - 1)
        nums = self.reverse(nums, 0, k - 1)
        nums = self.reverse(nums, k, len(nums) - 1)
        print(nums)

    def reverse(self, nums, start, end):
        print("reversing nums", nums)
        print("start index", start)
        print("end index", end)

        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
        return nums

