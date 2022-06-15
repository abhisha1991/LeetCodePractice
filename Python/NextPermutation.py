# https://leetcode.com/problems/next-permutation/
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # single digit numbers cannot have next greater
        if len(nums) == 1:
            return
        
        # find pos from right where the strictly decreasing criteria breaks
        # example, 564987 --> from the right, strictly decreasing criteria breaks at digit 4, ie, pos = 2 
        pos = None
        for i in range(len(nums)-1, -1, -1):
            prev = nums[i-1]
            cur = nums[i]
            # if cur happens to be greater than the previous digit, then the criteria is broken
            if cur > prev:
                pos = i-1
                break
        
        # if we were unable to find a strictly decreasing criteria from the right, example, 321
        # then there cannot be a next larger permutation/number
        # pos will be < 0 for the cases where the first digit is the largest
        if pos == None or pos < 0:
            # if we have reached last permutation, then we are expected to return the first permuation
            # ie, if input if 3,2,1 --> we need to return 1,2,3
            # so just reverse the number
            
            i = 0
            j = len(nums)-1
            while i < j:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                
                i+=1
                j -=1
                
            return
        
        # find the position of the digit to the right of pos that is just greater than nums[pos]
        nxtGreaterPos = None
        mn = sys.maxsize
        
        for i in range(pos+1, len(nums)):
            diff = nums[i] - nums[pos]
            if diff > 0 and mn > diff:
                mn = diff
                nxtGreaterPos = i
        
        # swap pos and nxtGreaterPos
        # in example above: 564987, pos = 2, ie nums[2] = 4, nxtGreaterPos = 5, ie, nums[5] = 7
        # swap 4 and 7 --> 567984 -- this is not the next greatest though
        tmp = nums[pos]
        nums[pos] = nums[nxtGreaterPos]
        nums[nxtGreaterPos] = tmp

        # we need to sort the stuff after pos+1, ie, [5,6,7] + [4,8,9] --> 567489
        # -- this is next greatest after 564987
        # this is the final answer, which we store in arr
        # so just copy this into nums (since we have to return in place answer)
        arr = nums[:pos+1] + sorted(nums[pos+1:])
        
        i = 0
        while i < len(nums):
            nums[i] = arr[i]
            i +=1