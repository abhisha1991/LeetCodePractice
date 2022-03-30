# https://leetcode.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # read up on sentinal nondes
        # these are just dummy nodes that serve a purpose of being in front of the head
        # imagine a case where the elements to delete were in the front of the list
        # in such a case, we'd have to handle edge cases in a special way
        # sentinal nodes allow us to point to the head (becoming a pseudo head)
        # this allows those edge cases to be handled in a uniform manner
        sent = ListNode('#', head)
        
        cur = head
        prev = sent
        
        while cur is not None:
            # we are at the sentinal node
            # so move to the next node
            if cur.val == '#':
                cur = cur.next
                continue
            
            # if we reach the to-delete val
            if cur.val == val:
                # check if we're at the end of the list
                # if not, then its a normal case
                # "skip" the to-delete node - which "deletes" it from linked list
                if cur.next is not None:
                    cur = prev
                    cur.next = cur.next.next
                # we are at the end of the list
                # so handle cur.next to avoid null ref exception
                else:
                    cur = prev
                    cur.next = None
            
            # we didn't match a value
            # so just move along the list as usual
            else:
                prev = cur
                cur = cur.next
        
        # sent.next will be pointing to the "head"
        return sent.next