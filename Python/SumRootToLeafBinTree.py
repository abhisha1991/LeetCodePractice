# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/submissions/
class Solution(object):
    def __init__(self):
        self.sum = 0
        
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root, "")
        return self.sum
    
    def helper(self, root, num):
        if root == None:
            return
        
        if root.left == None and root.right == None:
            n = int(num + str(root.val), 2)
            self.sum += n
        
        self.helper(root.left, num + str(root.val))
        self.helper(root.right, num + str(root.val))
        