import sys
# https://leetcode.com/problems/first-missing-positive/description/
# https://www.youtube.com/watch?v=8g78yfzMlao
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # as mentioned in other solution, negative numbers are not needed since we're finding only positive numbers
        # set negatives to 0, we'll need to "use" negative notation on a number later on
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0 
        
        # observe what we're doing here
        # we're taking a number in the array, note we're only interested in positive numbers, ie, val is abs()
        # and we're deriving an index from it, ie, idx = val-1 (just an arbitrary rule)
        # then we "create a mapping of this val to a place in our arr" located at nums[val-1]
        # now we're using a negative sign to "mark" that a given number val is present
        # so in essence we're using the array itself as a dictionary to "mark the presence" of a number, ie, val
        
        # imagine if there were two duplicate values present in array, say the number 3 was present twice
        # in that case, val = 3, idx = 2, we would go to nums[2], say it was 6 and we would convert nums[2] = -6
        # if the first 3 in the arr has already done this, then the second 3 need not do it again --
        # hence the "if nums[idx] > 0" condition. 
        # If it attempted to, then it would "reverse" the effect of the first 3, ie, nums[2]=6, thus unmarking "3"
        for i in range(n):
            val = abs(nums[i])
            idx = val-1
            if 0 <= idx < n:
                if nums[idx] > 0:
                    nums[idx] = -1 * nums[idx]
                elif nums[idx] == 0:
                    nums[idx] = -sys.maxsize
        
        # here i is referring to our missing number
        # we are going to go from 1 (smallest positive int) to n+1 (just bigger than array)
        for i in range(1,n+1):
            if nums[i-1] >= 0:
                return i
            
        return n+1
    
    # this is still o(n) memory, we need an o(1) memory solution, see above
    def firstMissingPositive2(self, nums: List[int]) -> int:
        h = set(nums)
        # the answer can lie only between 1 and len(nums)+1
        # say if you have an array [1,2,50] --> ans is 3
        # this is because we're looking for the smallest positive number not in array, so only len of array matters!
        
        # also note that 0 and negative numbers dont mean anything to us
        for i in range(1, len(h)+1):
            if i not in h:
                return i
        
        return len(h)+1