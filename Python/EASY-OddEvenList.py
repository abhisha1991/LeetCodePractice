# https://leetcode.com/problems/odd-even-linked-list/description/
class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        p = head
        q = head.next
        if q is None:
            return p
        if q.next is None:
            return p

        # store the start points of p and q - ie - first and second elements
        pstart = p
        qstart = q
        # we have atleast 3 nodes we know
        while q is not None and p.next.next is not None:
            # try 1->2->3->4->5->None
            # try 1->2->3->4->5->6->None
            p.next = p.next.next
            q.next = q.next.next
            p = p.next
            q = q.next

        if p.next is q:
            p.next = qstart
        return pstart