'''
DoorDash - Phone Screen

Given an array of A, a non-negative integer target. 
Each decimal in A needs to be operated by ceil or floor, and finally an integer array is obtained, 
requiring the sum of all integers that are in the array to be equal to target, and requiring adjustments sum of the decimal array is minimum.

Such as 
ceil(1.2) = 2, adjustment is 0.8,
floor(1.2) = 1, adjustment is 0.2. 

Return the integer array.

Input: A = [2.4,2.5], target = 5
Output: [2, 3], total adjustment = 0.9
        [3, 2], total adjustment = 1.1

so [2,3] is the answer since adjustment is minimum
'''
import math
import sys
class Solution():
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        self.adj = sys.maxsize
        self.output = None
        
    def func(self):
        
        def dfs(arr, left, adj, output):
            if left == 0 and len(arr) == 0:
                if adj < self.adj:
                    self.output = output               
                self.adj = min(self.adj, adj)
                return
            
            if not arr:
                return
            
            first = arr[0]
            ceiling = math.ceil(first)
            floor = math.floor(first)
            adj1 = ceiling - first
            adj2 = first - floor
            
            dfs(arr[1:], left-ceiling, adj + adj1, list(output + [ceiling]))
            dfs(arr[1:], left-floor, adj + adj2, list(output + [floor]))
        
        dfs(self.nums, self.target, 0, [])
        return self.output

s = Solution([2.4,2.5], 5)
print(s.func())

s = Solution([2.4,2.5,1.4,1.1,2.9], 10)
print(s.func())

s = Solution([-2.4,2.5,1.4,1.1,2.9], 10)
print(s.func())

s = Solution([-2.4,-2.5,-1.4,-1.1,-2.9], -10)
            # -2,  -3,   -1,   -1,  -3
print(s.func())

s = Solution([], -10)
print(s.func())

s = Solution([1,2,3,4,5], -10)
print(s.func())

s = Solution([-1,2,-3,4,-5], -3)
print(s.func())