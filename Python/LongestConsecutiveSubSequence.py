# https://leetcode.com/problems/longest-consecutive-sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        
        mx = 0
        for i in numset:
            # this if statement is ensuring that we are getting the smallest number as a start point
            # this avoids the work of finding out the longest sequence for numbers larger
            # imagine if we have [3,4,2,100,1,54,55,56]
            # this will only execute for 1, 54 and 100
            # that is, we save execution of while loop for each of 2,3,4 and 55,56
            if i-1 not in numset:
                num = i
                count = 1
                while num + 1 in numset:
                    count +=1
                    num +=1
                    
                if mx < count:
                    mx = count
        return mx