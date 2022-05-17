# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        # stores level as key, list of nodes at the level (from left to right) as value
        dic = defaultdict(list)
        q = [(root, 0)]
        while q:
            first, lvl = q.pop(0)
            if lvl not in dic:
                dic[lvl] = [first.val]
            else:
                dic[lvl].append(first.val)
            
            if first.left is not None:
                q.append((first.left, lvl+1))
            
            if first.right is not None:
                q.append((first.right, lvl+1))
        
        mxlvl = max(dic.keys())
        ans = []
        for i in range(mxlvl+1):
            elements = dic[i]
            # reverse elements if it is an odd level
            if i % 2 == 1:
                elements = elements[::-1]
                
            ans.append(elements)
        return ans