# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
    def __init__(self):
        self.idx = -1
        self.minNumIdx = -1
    
    # gets the index correponding to the min number
    # https://github.com/abhisha1991/LeetCodePractice/blob/master/Python/FindMinInSortedArray.py
    def helperMinPointIdx(self, numbers, low, high, n):
            if low > high:
                return
            
            mid = int((low + high)/2)      
            # print(f"mid is {mid}, low is {low} and high is {high}")
            if mid == 0 and numbers[mid] < numbers[mid+1] and numbers[mid] < numbers[-1]:
                self.minNumIdx = mid
                
            elif mid == n-1 and numbers[mid] < numbers[mid-1] and numbers[mid] < numbers[0]: 
                self.minNumIdx = mid
            
            elif mid-1 >= 0 and mid+1 < n and numbers[mid] < numbers[mid-1] and numbers[mid] < numbers[mid+1]:
                self.minNumIdx = mid

            self.helperMinPointIdx(numbers, low, mid-1, n)
            self.helperMinPointIdx(numbers, mid+1, high, n)
        
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        if n == 1:
            if nums[0] == target:
                return 0
            return -1
        
        def binsearch(low, high):
            if low > high:
                return 
            
            mid = int((low + high)/2)
            if nums[mid] == target:
                self.idx = mid
                return
            
            # target is smaller than element at mid, so target must be in the left side
            if nums[mid] > target:
                return binsearch(low, mid-1)
            # opposite case
            elif nums[mid] < target:
                return binsearch(mid+1, high)
        
        # get the index corresponding to the min point
        # everything to the right of this index should be in increasing order
        # everything to the left of this index (starting from 0 up to this index) should also be in increasing order
        # now we can perform binsearch on the 2 sub arrays against the target since they're sorted
        self.helperMinPointIdx(nums, 0, n-1, n)
        
        # print(f"min num index is {self.minNumIdx}")
        
        binsearch(0, self.minNumIdx)
        binsearch(self.minNumIdx, n-1)
        
        return self.idx