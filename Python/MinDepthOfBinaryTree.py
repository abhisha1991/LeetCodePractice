# https://leetcode.com/problems/minimum-depth-of-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.depth = sys.maxint
        
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.helper(root, 0)
        return self.depth
    
    def helper(self, root, d):
        if not root:
            return
        
        d +=1 
        if not root.left and not root.right:
            self.depth = min(d, self.depth)
            
        self.helper(root.left, d)
        self.helper(root.right, d)
        