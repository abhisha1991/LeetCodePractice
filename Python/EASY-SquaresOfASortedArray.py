#https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    # this is o(n) solution, vs squaring each element and sorting - which is o(n logn)
    # the complication arises from the fact that you could have negative numbers in the front
    # say [-4,-3,0,1,10] -- in this case, you cant just square numbers and return since it will be [16,9,0,1,100]
    # that's why we use 2 ptrs left and right and fill the result from the right
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        res = [0] * len(nums)
        
        k = len(nums)-1
        
        while l <= r:
            if nums[l]**2 > nums[r]**2:
                res[k] = nums[l]**2
                k -=1
                l +=1
            else:
                res[k] = nums[r]**2
                k -=1
                r -=1
                
        return res