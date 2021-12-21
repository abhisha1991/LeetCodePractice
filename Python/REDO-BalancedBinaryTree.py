# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/balanced-binary-tree/submissions/
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.helper(root) != -1
    
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        return 1 + max(left, right)

# easier to understand, uses o(n) space though
class Solution2(object):
    def __init__(self):
        self.dic = dict()
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.helper(root)
        for k, v in self.dic.items():
            if v > 1:
                return False
        return True
    
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.dic[root] = abs(left-right)
        return 1 + max(left, right) # return depth