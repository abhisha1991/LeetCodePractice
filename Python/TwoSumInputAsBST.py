# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        self.dic = defaultdict(int)
        
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
            self.dic[node.val] += 1
            traverse(node.right)
        
        traverse(root)
        for i in self.dic.keys():
            if k-i != i and (k-i) in self.dic:
                return True
            if k-i == i and self.dic[i] > 1:
                return True
        
        return False