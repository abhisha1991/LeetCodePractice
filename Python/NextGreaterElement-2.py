class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        stack = []
        n2  = n * 2
        # look at NextGreaterElementInLL.py for a detailed solution
        # this is a variation
        # we are basically looping through the array twice, to consider the circular array constraint
        # we do i % n because we will end up getting the index itself when i goes from n..2n
        for i in range(n2):                
            # if stack is empty or current element is less than top of stack, then current element adds on to stack
            if not stack or nums[i % n] <= nums[stack[-1]]:
                stack.append(i % n)
                continue
            
            # if we have found a big element, then while we are larger than top of stack, keep making us as the result for the top of stack
            while stack and nums[i % n] > nums[stack[-1]]:
                res[stack.pop()] = nums[i % n]
            
            # finally, dont forget to add ourselves to the stack, as we need to find the next largest element for ourselves as well!!
            stack.append(i % n)
        
        return res