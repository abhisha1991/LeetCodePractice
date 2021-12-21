# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this is the new index of the array
        idx = 0
        # i is the current element under consideration
        for i in range(0, len(nums)):
            # we allow modification of nums only iff:
            # idx is less than 2 [ie - if there were only 2 elements]
            # or if the current number is not equal to ANY OF the previous 2 numbers of nums
            # note that the last 2 conditions will never be hit for idx < 2,
            # it only comes into play if there are 3 or more elements
            if idx < 2 or nums[i] != nums[idx - 1] or nums[i] != nums[idx - 2]:
                nums[idx] = nums[i]
                idx += 1
        print(nums)
        return idx

s = Solution()
s.removeDuplicates([1,1,1,2,3])
