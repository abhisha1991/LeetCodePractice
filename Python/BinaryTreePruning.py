# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/binary-tree-pruning/
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.traverse(root)
        
    def traverse(self, root):
        if root == None:
            return None
        
        if self.checkIfTreeHasAllZeros(root.left):
            root.left = None
        
        if self.checkIfTreeHasAllZeros(root.right):
            root.right = None
        
        self.traverse(root.left)
        self.traverse(root.right)
        return root
        
    
    def checkIfTreeHasAllZeros(self, root):
        if root == None:
            return True
        
        if root.val == 0:
            return self.checkIfTreeHasAllZeros(root.left) and self.checkIfTreeHasAllZeros(root.right)
        
        return False