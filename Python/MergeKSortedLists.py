# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # merge 2 sorted linked lists k-1 times, where k is the number of linked lists
    # https://github.com/abhisha1991/LeetCodePractice/blob/master/Python/MergeTwoLinkedLists.py
    # copying the function from above file
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None
        
        while len(lists) > 1:
            l1 = lists.pop()
            l2 = lists.pop()
            l = self.mergeTwoLists(l1, l2)
            lists.append(l)
        
        return lists[0]
    
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
                # pick head 1 and progress head1
                head.next = head1
                head1 = head1.next
            else:
                # pick head 2 and progress head2
                head.next = head2
                head2 = head2.next
            # no matter what, always progress head
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

    # inefficient since this uses o(n) extra space
    def mergeKLists_inefficient_space(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for l in lists:
            head = l
            while head:
                arr.append(head.val)
                head = head.next
        
        arr.sort()
        sent = ListNode('#')
        head = sent
        for a in arr:
            head.next = ListNode(a)
            head = head.next
            
            
        return sent.next