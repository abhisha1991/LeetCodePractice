# https://www.youtube.com/watch?v=vB-81TB6GUc
# https://leetcode.com/problems/product-of-array-except-self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l2r = [1] * n
        r2l = [1] * n
        res = [1] * n
        
        # move left to right and l2r[i] holds all products of numbers up to i-1
        for i in range(1, n):
            l2r[i] = nums[i-1] * l2r[i-1]
        
        # move right to left and r2l[i] holds all products of numbers from last element to i+1
        for i in range(n-2, -1, -1):
            r2l[i] = nums[i+1] * r2l[i+1]
        
        # for each element, we have products to its left, and products to its right
        # multiiply those 2 and we'll have products except self
        for i in range(n):
            res[i] = l2r[i] * r2l[i]
            
        return res
