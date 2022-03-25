# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
import sys
class Solution:
    def __init__(self):
        self.minNum = sys.maxsize
        
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <=2:
            return min(nums)
        
        # this is similar to binary search
        # where we divide and conquer
        # the idea is that we find a number whose left and right neighbors are larger than it
        # [6,7,1,2,3,4,5] --> notice this condition is only true for element 1
        def helper(numbers, low, high):
            if low > high:
                return
            
            mid = int((low + high)/2)      
            # print(f"mid is {mid}, low is {low} and high is {high}")
            
            # special case where left neighbor is last element of array
            if mid == 0 and numbers[mid] < numbers[mid+1] and numbers[mid] < numbers[-1]:
                self.minNum = numbers[mid]

            # special case where right neighbor is first element of array
            elif mid == n-1 and numbers[mid] < numbers[mid-1] and numbers[mid] < numbers[0]: 
                self.minNum = numbers[mid]
            
            elif mid-1 >= 0 and mid+1 < n and numbers[mid] < numbers[mid-1] and numbers[mid] < numbers[mid+1]:
                self.minNum = numbers[mid]

            helper(numbers, low, mid-1)
            helper(numbers, mid+1, high)
            
        helper(nums, 0, n-1)
        return self.minNum