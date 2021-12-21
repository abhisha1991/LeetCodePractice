# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        x = head
        while x != None:
            count += 1
            x = x.next

        countFront = count - n
        if countFront < 0:
            return head

        if countFront is 0:
            return head.next

        x = head
        i = 0
        while i < countFront - 1:
            x = x.next
            i += 1

        x.next = x.next.next
        return head