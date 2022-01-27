# https://leetcode.com/problems/odd-even-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        odd = head
        even = head.next
        
        if even is None:
            return head
        
        if even.next is None:
            return head
        
        first_even = head.next
        
        while odd is not None and even is not None:
            last_odd = odd
            
            odd.next = even.next
            odd = odd.next
            
            if odd is not None:
                even.next = odd.next
                even = even.next
        
        # this condition is important because its possible that the last odd is not updated 
        # consider working through 1,2,3 -- if the below condition wasn't there, last_odd == 1 and not 3
        if odd is not None:
            last_odd = odd
            
        last_odd.next = first_even
        return head