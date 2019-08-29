#https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        while root!=None:
            if root.val==val:
                return root
            if root.val < val:
                root = root.right
            else:
                root = root.left

        return root
