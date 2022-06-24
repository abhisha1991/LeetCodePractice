# https://leetcode.com/problems/sum-root-to-leaf-numbers
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        
        
        def helper(node, path):
            if not node:
                return
            
            # when the path is such that the current node is a leaf
            # then add to total
            if not node.left and not node.right:
                num = path + str(node.val)
                self.total += int(num)
            
            p = path + str(node.val)
            helper(node.left, p)
            helper(node.right, p)
        
        helper(root, '')
        return self.total