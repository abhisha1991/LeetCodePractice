# https://www.youtube.com/watch?v=kekmCQXYwQ0
# Kadanes algo
# https://leetcode.com/problems/maximum-subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start, end  = 0, 0
        maxSum = nums[0]
        sumSoFar = 0
        for i in range(len(nums)):
            sumSoFar += nums[i]
            # if we have a greater sum than what we have
            if sumSoFar > maxSum:
                maxSum = sumSoFar
                # start remains same, update end
                end = i
            # negative sum is a condition for resetting 
            # notice the below is an if, not an elif
            if sumSoFar < 0:
                sumSoFar = 0
                # update start to next index and hope to get better
                # outcomes going forward
                start = i+1
                
        return maxSum