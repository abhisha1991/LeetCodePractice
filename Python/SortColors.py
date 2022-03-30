# https://leetcode.com/problems/sort-colors
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # the idea is to have 2 pointers (left and right)
        # take 0 from the right, find a 1 or 2 from left and swap their positions
        # keep doing this until you've exhausted left and right pointers
        # repeat this with 1 (find 1 on the right), find a 2 on the left and swap 
        def helper(n):
            i = 0
            j = len(nums)-1
            while i < j:
                # keep decrementing j till you've found your desired n
                if nums[j] != n:
                    j -=1
                    continue
                
                # nums[j] holds desired n, if value on left (nums[i]) is > n
                # then swap
                if nums[i] > n:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                    j -=1
                i +=1
        
        helper(0)
        helper(1)
        # no need to call helper(2) because if 0,1 are sorted, then 2 is automatically sorted
            