# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/validate-binary-search-tree/description/
'''
Concept is very simple
Suppose you have a BST
      10
     /  \
    5   15
       /  \
      12  20
         /  \
        19   40

Then 10 > - infinte, 10 < infinite
5 > - infinite, 5 < 10
15 > 10, 15 < infinite
12 > 10, 12 < 15
'''

import sys
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, -sys.maxint, sys.maxint)

    def isValid(self, root, minval, maxval):
        if root == None:
            return True

        # if root violates the BST law, then its not a BST
        if root.val <= minval or root.val >= maxval:
            return False

        # in the left child, we should be > minval, less than the root
        # in the right child, we should be greater our parent, less than maxval
        return self.isValid(root.left, minval, root.val) and self.isValid(root.right, root.val, maxval)