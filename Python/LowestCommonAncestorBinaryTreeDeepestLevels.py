# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
from collections import defaultdict
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # do level order traversal of the binary tree
        q = [(root, 0)]
        lvlDic = defaultdict(list)
        while q:
            node, lvl = q.pop(0)
            
            lvlDic[lvl].append(node)
            if node.left:
                q.append((node.left, lvl+1))
            
            if node.right:
                q.append((node.right, lvl+1))
                
        
        # get max depth of the tree
        mxDepth = max(lvlDic.keys())
        
        # get first (left most) and last (right most) nodes that are at max level
        n1 = lvlDic[mxDepth][0]
        n2 = lvlDic[mxDepth][-1]
        
        # if they are the same, then there's only 1 node at that level, so we can return that node
        if n1 == n2:
            return n1
        
        # std lca function
        def lca(root, node1, node2):
            if not root or root == node1 or root == node2:
                return root
            
            left = lca(root.left, node1, node2)
            right = lca(root.right, node1, node2)
            
            if left and right:
                return root
            
            if not left:
                return right
            
            if not right:
                return left
            
            return None
        
        return lca(root, n1, n2)