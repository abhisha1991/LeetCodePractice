# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        nums = []
        # copy linked list into array
        while head != None:
            nums.append(head.val)
            head = head.next
        
        # initialize result with all 0s, why? because, generally, if there is no next greater element for curret element, answer is 0
        res = [0] * len(nums)
        stack = []
        # idx and n are the current index and number
        for idx, n in enumerate(nums):
            # this condition is clear
            if len(stack) == 0:
                stack.append(idx)
                continue
            
            # if our current element is less than top of stack, then we havent found a next greater element so far
            # so keep adding to the stack
            top = nums[stack[-1]]
            if n <= top:
                stack.append(idx)
                continue
            
            # here n ie, current element > top, so while this is true, keep popping and setting the next greatest element as "n" for all these numbers of top
            while len(stack) > 0 and n > top:
                res[stack.pop()] = n
                if len(stack) > 0:
                    top = nums[stack[-1]]
            
            # very important - dont forget to add "n" itself to the stack, else we wont have an answer for the element that helped others 
            stack.append(idx)
        
        return res
            