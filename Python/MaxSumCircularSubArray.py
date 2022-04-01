# https://leetcode.com/problems/maximum-sum-circular-subarray/
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        def kadanes(arr):
            maxSum = arr[0]
            sumSoFar = 0
            for i in range(len(arr)):
                sumSoFar += arr[i]
                if sumSoFar > maxSum:
                    maxSum = sumSoFar
                    
                if sumSoFar < 0:
                    sumSoFar = 0
            return maxSum
        
        # this is considering the entire array, getting the max sum without splitting / considering circular arrays
        ans = kadanes(nums)
        
        '''
        # this works, but is inefficient as its o(N2)
        # why? because we are splitting the arr by skipping the ith element into left and right
        # and we're performing kadanes - which is o(n) - on each of these subarrays
        # so time taken to split array is o(n) and within that we perform kadanes, so o(N2)
        # why does the splitting work? Kadanes works on an entire array, so to get a circular array, we need to do concat right with left
        # note that we concat right with left, and not left with right
        if len(nums) > 2:
            for i in range(len(nums)-1):
                if i == 0:
                    continue
                
                left = nums[0:i]
                right = nums[i+1:]
                ans = max(ans, kadanes(right + left))
        
        return ans
        '''
        
        # sum to the right, including yourself
        sumRight = [-sys.maxsize] * n
        sumRight[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            sumRight[i] = sumRight[i+1] + nums[i]
        
        # max sum to the right, either include yourself or not
        maxsumRight = [-sys.maxsize] * n
        maxsumRight[-1] = sumRight[-1]
        for i in range(n-2, -1, -1):
            # here the left arg is not including yourself, the right param is including yourself
            maxsumRight[i] = max(maxsumRight[i+1], sumRight[i])
            
        sumLeft = 0
        for i in range(n-2):
            sumLeft += nums[i]
            # note that we're skipping the i+1th element here
            # sumLeft includes sub array sum up to i (inclusive)
            # maxsumRight includes sub array sum up to i+2
            # so i+1 is intentionally left out, such that we can form a circular sub array
            # notice that originally ans contained subset sub including the whole array (without skipping elements)
            # so here we are considering all cases, whole array and circular array (skipping the i+1th element)
            ans = max(ans, sumLeft + maxsumRight[i+2])
            
        return ans