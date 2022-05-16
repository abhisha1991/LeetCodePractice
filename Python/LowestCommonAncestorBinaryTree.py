# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # the left or right being not null is an indication that p or q was found in the left/right dfs
        # if p is found in left sub tree of root, then returned value in 'left' is going to be node p
        # if q is found in right sub tree of root, then returned value in 'right' is going to be q
        # so if we were able to find p in left sub tree and q in right sub tree, then current node, ie, 'root'
        # must be the LCA
        if left and right:
            return root
        
        # we were only able to find one of the nodes (p or q) in the right sub tree
        if not left:
            return right
        
        # we were only able to find one of the nodes (p or q) in the left sub tree
        if not right:
            return left
        
        # neither p nor q were found in the left/right sub tree
        # can happen in scenario where p = 2, q = 4 in the tree below
        '''
                 1
               /   \
              5     3
             / \   / \
            2   4 6   7
            
        in this case, when we're traversing the path 1-> (3,6,7), 
        we would return None from both left/right sub trees since both p,q are at left of 1
        '''
        return None