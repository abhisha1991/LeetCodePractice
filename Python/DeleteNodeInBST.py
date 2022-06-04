# https://leetcode.com/problems/delete-node-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        self.keyFound = False
        parent = dict()
        self.key = key
        
        def traverse(node, p):
            if not node:
                return
            
            parent[node] = p
            
            if node.val == self.key:
                self.keyFound = True
            
            traverse(node.left, node)
            traverse(node.right, node)
        
        traverse(root, None)
        
        # if key doesn't exist, return tree unmodified
        if not self.keyFound:
            return root
        
        # find details about the element to remove, including its parent
        for k,v in parent.items():
            if k.val == self.key:
                remove = k
                pRemove = parent[k]
                break
        
        # if item to delete is root node
        if pRemove is None:
            if remove.left is None and remove.right is None:
                return None
            
            if remove.left is None:
                return remove.right
            
            if remove.right is None:
                return remove.left
            
            '''
                     5 <--- node to delete
                   /    \ 
                  3        90
                 / \     /    \
                2   4   60     100
                       /
                      54
                      
            
            so if we have to delete root, we can just take the left sub tree of root and dock it under the smallest
            element of the right sub tree, ie, 54
            
                     90
                   /    \
                  60     100
                 /
                54 
               /
              3
             / \
            2   4
            
            so how to find 54? do root.right and then keep going left to find the smallest node in the right subtree
            '''
            x = root.right
            while x.left:
                x = x.left
            
            x.left = root.left
            return root.right
        
        # if item to delete is a leaf
        if remove.left is None and remove.right is None:
            if pRemove.left == remove:
                pRemove.left = None
            else:
                pRemove.right = None
            return root
        
        '''
                4
                 \
                  7
                 / \ 
                6   80
               /   /  \ 
              5   10  90
        
        remove 7 say, in that case we need to get something like
                 
                 4 <-- pRemove
                  \
                   80 <-- remove.right, ie, x
                  / \
                10   90
                /
               6
              /
             5 
        
        so first, we need to check if remove.right exists or not, ie, 80 exists or not
        then we need to make 80 the child of 4
        then we need to find the smallest element in the 80 sub tree, which is 10 
        
        then we need to attach the left sub tree of 7, ie (6 --> 5) under 10
        '''
        
        # if item to delete is a regular node
        if remove.right:
            x = remove.right
            # establish link between parent and child of remove
            if pRemove.val <= x.val:
                pRemove.right = x
            else:
                pRemove.left = x
            
            # find the smallest element in the left sub tree of the child that will succeed the removed node
            # 80 is the successor in the above example, and 10 is the smallest element in its left sub tree
            while x.left:
                x = x.left
            
            # make the left sub tree of 10 have the left sub tree of the removed node (ie, 6 --> 5)
            x.left = remove.left
            
            # return the original root, which contains the modified links
            return root
        
        # same idea if remove.right was null but remove.left was not null
        else:
            x = remove.left
            if pRemove.val <= x.val:
                pRemove.right = x
            else:
                pRemove.left = x
                
            while x.right:
                x = x.right
            x.right = remove.right
            return root