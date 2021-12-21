# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
import sys
class Solution:
    def __init__(self):
        self.maxi = -sys.maxsize

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.maxi

    def helper(self, root):
        if root is None:
            return 0

        left = max([0, self.helper(root.left)])
        right = max([0, self.helper(root.right)])
        # print("left is " + str(left) + " for root " + str(root.val))
        # print("right is " + str(right) + " for root " + str(root.val))
        self.maxi = max([self.maxi, left + right + root.val])
        return max([left, right]) + root.val
