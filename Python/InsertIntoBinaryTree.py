# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/insert-into-a-binary-search-tree/ 
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        rootx = root
        self.insert(root, val)
        return rootx
        
    def insert(self, root, val):
        
        if root == None:
            return None
        
        rootBigger = root.val > val
        
        if rootBigger and root.left == None:
            root.left = TreeNode(val)
            return root
        
        elif rootBigger == False and root.right == None:
            root.right = TreeNode(val)
            return root
        
        elif rootBigger:
            return self.insert(root.left, val)
        else:
            return self.insert(root.right, val)
        