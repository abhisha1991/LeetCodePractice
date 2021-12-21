# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# basically this is inorder traversal with the special condition that when k decrements to 0, we store our result

class Solution:
    def __init__(self):
        self.count = 0
        self.kthsmall = 0

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = k
        self.helper(root)
        return self.kthsmall

    def helper(self, root):
        if root is None:
            return
        self.helper(root.left)
        self.count -= 1
        if self.count is 0:
            self.kthsmall = root.val
            return
        self.helper(root.right)