"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
# https://leetcode.com/problems/n-ary-tree-postorder-traversal
class Solution(object):
    def __init__(self):
        self.res = []
        
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.helper(root)
        return self.res
    
    def helper(self, root):
        if not root:
            return
        
        for c in root.children:
            self.helper(c)
        
        self.res.append(root.val)