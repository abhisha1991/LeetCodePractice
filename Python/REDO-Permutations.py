# https://leetcode.com/problems/permutations/description/
# basically uses DFS - need to understand more - https://leetcode.com/problems/permutations/discuss/18247
# look at this solution - it has a common backtacking template - https://leetcode.com/problems/permutations/discuss/18239
class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.helper(nums, 0)
        print("res is")
        print(self.res)
        return self.res

    def helper(self, nums, begin):
        if begin >= len(nums):
            print(nums)
            self.res.append(list(nums))
            return
        else:
            for i in range(begin, len(nums)):
                print("swapping nums", nums)
                nums = self.swap(nums, begin, i)
                print("new nums", nums)
                self.helper(nums, begin + 1)
                nums = self.swap(nums, begin, i)
                print("swapped back nums", nums)
                print("end of iteration i=", i)
                print("begin was", begin)

    def swap(self, nums, begin, i):
        temp = nums[i]
        nums[i] = nums[begin]
        nums[begin] = temp
        return nums
