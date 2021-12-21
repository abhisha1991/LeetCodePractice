# https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        dic = dict()
        for i in nums:
            dic[i] = target - i

        ans = set()
        for k, v in dic.items():
            if v in dic.keys():
                ans.add(nums.index(k))
                ans.add(nums.index(v))
                break

        if len(ans) == 2:
            return list(ans)

        for i in range(len(nums)):
            if nums[i] == nums[list(ans)[0]] and i != list(ans)[0]:
                ans.add(i)
                return list(ans)

        return []


s = Solution()
s.twoSum([1, 2, 3, 4, 5, 6], 10)
s.twoSum([1, 1, 3, 4, 6, 6], 12)