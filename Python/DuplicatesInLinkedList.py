# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        head1 = head
        while head != None:
            value = head.val
            follow = head.next
            while follow != None and value == follow.val:
                follow = follow.next
            head.next = follow
            head = head.next
            
        return head1