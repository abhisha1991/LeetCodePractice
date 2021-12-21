# https://leetcode.com/problems/linked-list-cycle-ii/description/
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        q = head
        flag = False
        if head == None:
            return None
        while p != None and q != None and q.next != None:
            q = q.next.next
            p = p.next
            if p == q:
                print("There is a loop at this linked list - common point", p.val)
                flag = True
                break

        if flag is False:
            return None
        # figure out start of the cycle loop
        # watch this video for proof as to why this is the start of the loop
        # https://www.youtube.com/watch?v=LUm2ABqAs1w
        p = head
        while p != q:
            p = p.next
            q = q.next
        return p