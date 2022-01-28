# https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if other in dic.keys():
                return [i, dic[other]]
            else:
                dic[nums[i]] = i
        return []


s = Solution()
s.twoSum([1, 2, 3, 4, 5, 6], 10)
s.twoSum([1, 1, 3, 4, 6, 6], 12)