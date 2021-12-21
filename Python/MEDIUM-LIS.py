# https://leetcode.com/problems/longest-increasing-subsequence/description/
# This below is O(n2) which is good, but not optimal, optimal is O(nlog(n)) - will have to look this up

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        lis = [1] * len(nums)
        i = 1
        j = 0
        while i < len(nums):
            if j == i:
                j = 0
                i += 1
                continue
            if nums[j] < nums[i]:
                lis[i] = max([lis[i], 1 + lis[j]])
            j += 1

        return max(lis)