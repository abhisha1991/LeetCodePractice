# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        x = headA
        y = headB
        countA = 0
        countB = 0

        while x != None:
            x = x.next
            countA += 1

        while y != None:
            y = y.next
            countB += 1

        diff = abs(countA - countB)
        x = headA
        y = headB
        count = 0
        if countA > countB:
            while count < diff:
                x = x.next
                count += 1
        elif countB > countA:
            while count < diff:
                y = y.next
                count += 1

        while x != y and x is not None and y is not None:
            x = x.next
            y = y.next

        return x




