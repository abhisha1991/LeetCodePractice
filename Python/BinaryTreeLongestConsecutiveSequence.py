# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.mxlen = 0
        if not root:
            return 0
        
        def dfs(node, parent, length):
            if not node:
                return
            
            # as long as child is one more than parent value, then increment length
            if parent and node.val == parent.val + 1:
                length +=1
            
            # if the node and its parent are not 1 unit apart, then reset the length to 1
            # why reset to 1? because you're counting the current node as the starting point
            if parent and node.val != parent.val + 1:
                length = 1
            
            self.mxlen = max(self.mxlen, length)
            dfs(node.left, node, length)
            dfs(node.right, node, length)
        
        dfs(root, root, 0)
        return self.mxlen