# https://leetcode.com/problems/single-element-in-a-sorted-array/
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.binsearch(0, len(nums)-1, nums)
        
    def binsearch(self, lo, hi, nums):
        if lo < hi:
            mid = int((lo+hi)/2)
            # in a perfect world -- 1,1,2,2,3,3,....
            # the first of the pair is always even index
            # the 2nd element of the pair is always odd index
            # so we assume we're in a perfect world and if we land on an odd number
            # we move back 1 step and come to the supposed start of the "pair"
            # check if this index (even/start of pair) and the next (odd/end of pair) 
            # if these are equal, if they are equal, then everything up till this pair is fine, so check right hand side - else check left hand side.
            if mid % 2 == 1:
                mid -=1
            if nums[mid] == nums[mid+1]:
                # check rhs of array by updating lo
                lo = mid+2
            else:
                # check lhs of array by updating hi
                hi = mid-1
            return self.binsearch(lo, hi, nums)
        return nums[lo]

'''
trace: 1,1,2,3,3,4,4,8,8
index: 0,1,2,3,4,5,6,7,8

2nd solution:
1 liner - although it is O(n)
2 * sum(set(array)) - sum(array)
so imagine if you have [1,1,2,3,3]
2 * sum([1,2,3]) - sum([1,1,2,3,3]) = 2

3rd solution:
xor - again O(n)
[1,1,2,3,3]
https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/316908/Fastest-Solution
if you start with 0
if you xor any number with itself, it will be 0
so 1 xor 1 = 0
and 3 xor 3 = 0
and 0 xor 0 = 0 [from the result of the above xors]
finally, 0 xor 2 = 2 [any number xored with 0 is itself], 
so you're left with the 1 number that didnt have a pair and was finally xored with 0
'''