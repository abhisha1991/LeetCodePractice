# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def __init__(self):
        self.elements = set()
        
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        if root.left == None and root.right == None:
            return -1
        
        self.helper(root)
        arr = list(self.elements)
        arr.sort()
        if len(arr) == 1:
            return -1
        
        return arr[1]
        
    def helper(self, root):
        if not root:
            return
        
        self.elements.add(root.val)
        self.helper(root.left)
        self.helper(root.right)