# https://leetcode.com/problems/range-sum-query-immutable
class NumArray:

    def __init__(self, nums: List[int]):
        # the tricky thing here to recognize is that we need an extra 0 on the left
        self.prefix = [0] * (len(nums)+1)
        
        # prefix sum for the first element in nums starts at index 1
        for i in range(0, len(nums)):
            self.prefix[i+1] = self.prefix[i] + nums[i]
        
        
    def sumRange(self, left: int, right: int) -> int:
        # notice how we're doing right+1 for the right index
        return self.prefix[right+1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)