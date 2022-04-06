# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # create a sentinel node
        sent = ListNode('#')
        head = sent
        
        head1 = list1
        head2 = list2
        
        # since there are only 2 nodes, so we can compare element by element
        # and merge them as we go along
        # 0 --> 3 --> 4 (list1)
        # 1 --> 2 --> 4 (list2)
        # we compare 0 (head1) and 1 (head2), pick 0, make head.next --> 0
        # move head1 ahead to 3 since it was picked, head2 remains where it is, at 1
        # move head always, head is at 0 now, now repeat, compare head1 and head2 
        # until both lists have exhausted
        
        while head1 and head2:
            h1 = head1.val
            h2 = head2.val
            if h1 <= h2:
                # pick head 1
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            
            head = head.next        
        
        # at this point, one of list1 or list2 is complete
        # whichever is shorter is typically complete
        # only 1 of the 2 below while loops will execute
        while head1:
            head.next = head1
            head = head.next
            head1 = head1.next
        
        while head2:
            head.next = head2
            head = head.next
            head2 = head2.next
        
        # return start of the linked list
        return sent.next