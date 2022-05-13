# https://leetcode.com/problems/maximum-product-subarray
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            # have 3 options at any stage
            # choose existing number as is, this may be preferred when we just encountered a 0 and are starting from scratch with curr
            # choose max so far x curr - this will be preferred in the case where we have only positive numbers and non-decreasing product
            # choose min so far x curr - this may be preferred in a case where minSoFar is neg, and cur is neg, which can give us a big +ve
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)
            # print(f"for i={i}, cur is {curr}, tmp is {temp_max}, maxSoFar is {max_so_far}, minSoFar is {min_so_far}, res is {result}")
            
        return results