# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/path-sum/submissions/
class Solution(object):
    def __init__(self):
        self.ans = False
        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.helper(root, sum)
        return self.ans
    
    def helper(self, root, sum):
        if not root:
            return
        
        if sum - root.val == 0 and not root.left and not root.right:
            self.ans = True
            return
        
        self.helper(root.left, sum-root.val)
        self.helper(root.right, sum-root.val)