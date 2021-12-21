# https://leetcode.com/problems/move-zeroes/description/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        if len(nums) == 1:
            print(nums)
            return
        if len(nums) == 2 and nums[0] == 0:
            x = nums[1]
            nums[1] = 0
            nums[0] = x
            print(nums)
            return
        while j < len(nums):
            # 0 1 0 3 12
            if nums[i] == 0 and nums[j] != 0:
                # if curr is 0 and next is non zero
                temp = nums[j]
                nums[j] = 0
                nums[i] = temp
                i += 1
            # if curr and next are both 0, just move ahead
            elif nums[i] == 0 and nums[j] == 0:
                pass
            # IMPORTANT - ALMOST MISSED THIS ONE!
            elif nums[i] != 0:
                i += 1
            j += 1
        print(nums)

s = Solution()
s.moveZeroes([0, 1, 0, 3, 12])
s.moveZeroes([0, 0, 0, 0, 0])
s.moveZeroes([0, 1, 1, 1, 1])
s.moveZeroes([1, 1, 1, 1, 1])
s.moveZeroes([1, 0, 1])
s.moveZeroes([1])
