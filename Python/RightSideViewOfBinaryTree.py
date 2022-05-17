# https://leetcode.com/problems/binary-tree-right-side-view
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        self.lvlDic = defaultdict(list)
        # do simple bfs, (node, level) are elements in the queue
        q = [(root, 0)]
        while q:
            first, lvl = q.pop(0)
            
            # add level as key and node as value
            if lvl not in self.lvlDic:
                self.lvlDic[lvl] = [first]
            else:
                self.lvlDic[lvl].append(first)
                
            if first.left is not None:
                q.append((first.left, lvl+1))
            
            if first.right is not None:
                q.append((first.right, lvl+1))
            
        
        # last element at each level is going to be the rhs view of the tree
        # first element at each level is going to be the lhs view of the tree
        mxlvl = max(self.lvlDic.keys())
        ans = []
        for i in range(mxlvl+1):
            elements = self.lvlDic[i]
            ans.append(elements[-1].val)
        return ans