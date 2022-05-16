# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        self.head = None
        self.tail = None
        '''
                    4
                  /   \
                 2     5
                / \
               1   3
        
        we need to do inorder here, why?
        because inorder is LNR --> if we apply it to the above, we end up getting sorted order
        ie, we get 1,2,3,4,5
        
        now the 'head' of the linked list is going to be the left most element, 
        ie, smallest element, ie, 1 in this case
        
        the 'tail' is going to be the right most element, ie, 5 in this case
        '''
        
        def helper(root):
            if not root:
                return None
            
            # notice that we're doing inorder
            helper(root.left)
            
            # if we haven't initialized head yet, then set it to left most element (current root)
            # this is guaranteed to be left most element (1 in our example)
            # because we are going to be calling helper on root.left until we reach 1 as seen above
            if not self.head:
                self.tail = root # set both tail and head as 1
                self.head = root
            else:
                # regular recursion case
                # take node 2's traversal right after node 1
                # current tail is 1, so we're saying:
                # 1.right = 2
                # 2.left = 1 (set up circular pointer between 1 and 2)
                # update ONLY the tail (not the head) to be current root, ie, 2
                
                # take node 3's traversal right after node 2 (inorder LNR)
                # current tail is 2 (from above), so we're saying
                # 2.right = 3
                # 3.left = 2 (set up circular pointer between 2 and 3)
                # update ONLY the tail to be current root, ie, 3
                # so notice that we're shifting the tail by 1 every time
                self.tail.right = root 
                root.left = self.tail
                self.tail = root
            
            helper(root.right)
        
        helper(root)
        # after the above happens, we'll have something like
        '''
        legend: ==== means there's left/right connections between both nodes
        
            1 ==== 2 ==== 3 ==== 4 ==== 5
        
        but we still need to do 1.left = 5 and 5.right = 1
        1 = head
        5 = most recent tail
        '''
        self.head.left = self.tail
        self.tail.right = self.head
        
        # return head of Linked list
        return self.head