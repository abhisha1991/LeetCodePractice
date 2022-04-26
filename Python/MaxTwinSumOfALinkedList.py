# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        i = 0
        dic = dict()
        l = head
        n = 0
        while l != None:
            n +=1
            l = l.next
            
        l = head
        # iterate into half of the linked list and assign l.val as dictionary value
        for i in range(int(n/2)):
            dic[i] = l.val
            l = l.next
        
        # note at this point "l" has already reached mid way of linked list
        # notice how we're starting j's iteration from i+1, this is the twin part of the calculation
        for j in range(i+1, n):
            # calcualate twin index, which should match what we have put into dic already
            idx = n-1-j
            
            # add the twin index value to original value
            dic[idx] += l.val
            l = l.next
        
        # return max sum of twin index and original index
        return max(dic.values())