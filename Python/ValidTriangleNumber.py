# https://leetcode.com/problems/valid-triangle-number/
from itertools import combinations
import bisect
class Solution:
    # gets a TLE since we're generating all combinations
    def triangleNumber2(self, nums: List[int]) -> int:
        count = 0
        
        for c in combinations(nums, 3):
            # 3 sides of the triangle
            x = c[0]
            y = c[1]
            z = c[2]
            
            if x + y > z and y + z > x and z + x > y:
                count +=1
                
        return count

    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        # since input can have 0, and a side of a triangle cannot be 0, we ignore 0s
        nums = [x for x in nums if x != 0]
        
        n = len(nums)
        
        for i in range(0, n):
            for j in range(i+1, n):
                # i is the 1st side, j is second side, which can start from i+1
                # k is 3rd side, which can start from i+2
                # now k can increase beyond i+2 theoretically up till n-1

                # because nums is sorted with positive integers
                # we use binary search to find the max index of k, such that
                # nums[i] + nums[j] > nums[k] -- this is a condition for a valid triangle
                
                # in general, the valid condition is sum of any 2 sides > 3rd side
                # we don't care for nums[j] + nums[k] > nums[i] or  nums[i] + nums[k] > nums[j]
                # why? because nums is sorted and those 2 conditions are auto satisfied
                k = bisect.bisect_left(nums, nums[i] + nums[j])
                
                # ie, all triangles for fixed i,j and maximum ks are counted toward the answer
                # say if input was [6,10,11,12,13,14,15,16,20] and i=0, j=1, ie, 6 and 10
                # then side k can be 11, 12, 13, 14, 15, ie, max k can be index of 15, ie, k=6
                # note that bisect left above will give value 7, that is why we do k-1 below
                count += (k-1)-j
        
        return count