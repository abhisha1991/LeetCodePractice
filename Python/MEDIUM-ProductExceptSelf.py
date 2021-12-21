# https://www.youtube.com/watch?v=vB-81TB6GUc
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0 or len(nums) == 1:
            return nums

        prod = 1
        # initialize array of 1
        output = [1] * len(nums)
        # get left product
        for i in range(1, len(nums)):
            prod = prod * nums[i - 1]
            output[i] = prod

        prod = 1
        # get right product
        for i in range(len(nums) - 2, -1, -1):
            prod = prod * nums[i + 1]
            # make sure you multiply with output[i] in RHS since its value may no longer be 1
            output[i] = output[i] * prod

        return output
