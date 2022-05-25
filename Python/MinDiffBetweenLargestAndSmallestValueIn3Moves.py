# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # if we have array of 4 or less elements, we can change up to 3 of them to match 4th element
        # which gives us a diff of 0
        if len(nums) <=4:
            return 0
        
        # sort array so we can know what values we're manipulating
        '''
        say if your array had 6 elements, [a1, a2, a3, a4, a5, a6] in sorted order
        now we can make 0 changes --> diff is a6-a1
        or we can make 1 change from right (make a6 = a1) --> diff is a5-a1
        or we can make 2 changes from right (make a6, a5 both = a1) --> diff is a4-a1
        or we can make 3 changes from right (make a6, a5, a4 all = a1) --> diff is a3-a1
        or we can make 1,2, or 3 changes from the left
        or we can make 2 changes --> 1 from left, 1 from right
        or we can make 3 changes --> (1L,2R), (2L,1R)
        '''
        nums.sort()
        n = len(nums)
        # base case, 0 changes
        result = max(nums) - min(nums)
        for i in range(4):
            result = min(result, nums[n - 1 - 3 + i] - nums[i])
        return result