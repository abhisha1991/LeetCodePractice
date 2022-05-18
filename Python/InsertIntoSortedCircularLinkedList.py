# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        # single node in linked list
        if head.next == head:
            n = Node(insertVal)
            n.next = head
            head.next = n
            return head
        
        # find first smallest element
        # in case of multiple smallest elements, this picks first
        smallest = head
        cur = head.next
        v = head.val
        while cur != head:
            # pick first smallest
            if cur.val < v:
                smallest = cur
                v = smallest.val
            cur = cur.next
        
        # find last largest element
        # in case of multiple largest elements, this picks last
        largest = head
        cur = head.next
        v = head.val
        while cur != head:
            # pick last largest
            if cur.val >= v:
                largest = cur
                v = largest.val
            cur = cur.next
        
        # print(f"head is {head.val}")
        # print(f"largest is {largest.val}")
        # print(f"smallest is {smallest.val}")
        
        # create node with insertVal
        n = Node(insertVal)
            
        if insertVal >= largest.val:
            # find node just after largest, call it nxt
            nxt = largest.next
            # insert n between largest and nxt
            largest.next = n
            n.next = nxt
        elif insertVal <= smallest.val:
            # find node just before smallest, call it cur
            cur = smallest
            while cur.next != smallest:
                cur = cur.next
            # insert n between cur and smallest
            cur.next = n
            n.next = smallest
        else:
            # insert in between
            cur = smallest
            prev = None
            # find the prev, cur nodes such that n's value is in between prev and cur
            # ie, prev.val <= n.val <= cur.val
            while cur.val < n.val:
                prev = cur
                cur = cur.next
            # once we have found prev and cur, insert n between these
            prev.next = n
            n.next = cur
        
        # always return head
        return head