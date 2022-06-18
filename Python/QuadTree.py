# https://leetcode.com/problems/construct-quad-tree
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
'''
1. Start with the full grid and keep on diving it four parts.
2. Once we have a grid of size 1 then start with merging.
3. Compare if all parts are leaf nodes,
    if yes then merge all into a single node.
    else, return all four nodes separately.
'''
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, length):
            if length == 1:
                return Node(grid[r][c] == 1, True, None, None, None, None)
            else:
                half = length // 2
                # take top left as reference point (0,0)
                # top right's start will be (0, 0 + half)
                # bottom left's start will be (0 + half, 0)
                # bottom right's start will be (0 + half, 0 + half)
                
                tLeft = dfs(r, c, half)
                tRight = dfs(r, c + half, half)
                bLeft = dfs(r + half, c, half)
                bRight = dfs(r + half, c + half, half)
                
                if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf: 
                    if tLeft.val == tRight.val == bLeft.val == bRight.val:
                        # if all parts are leaves and all val are the same, ie, either all are true or all are false
                        # then we can create a new node:
                        # 1. with isLeaf = True, 
                        # 2. with val = any of the vals in the sub parts
                        # 3. with all its sub parts equal to None
                        return Node(tLeft.val, True, None, None, None, None)
                
                # else the node is not a leaf and we need to break down further
                # give a dummy value for val since we haven't reached a single node situation in all 4 parts
                return Node('dummy', False, tLeft, tRight, bLeft, bRight)
            
        
        return dfs(0, 0, len(grid))