# https://leetcode.com/problems/find-largest-value-in-each-tree-row/ 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = []
        
        if not root:
            return []
        
        # store node and level in the queue
        q.append((root, 0))
        # levels is the dictionary that stores all the node values, left to right at a level
        levels = defaultdict(list)
        
        # do bfs
        while q:
            node, lvl = q.pop(0)
            levels[lvl].append(node.val)
            
            if node.left:
                q.append((node.left, lvl+1))
            
            if node.right:
                q.append((node.right, lvl+1))
            
            
        res = []
        last = max(levels.keys()) + 1
        for i in range(last):
            # store the largest node value per level in res
            res.append(max(levels[i]))
        
        return res