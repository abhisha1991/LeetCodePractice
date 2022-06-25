# https://leetcode.com/problems/find-mode-in-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dic = defaultdict(int)
        self.mxFreq = 0
        
        def helper(node):
            if not node:
                return
            
            self.dic[node.val] +=1
            self.mxFreq = max(self.mxFreq, self.dic[node.val])
            
            helper(node.left)
            helper(node.right)
        
        helper(root)
        res = []
        for k,v in self.dic.items():
            if v == self.mxFreq:
                res.append(k)
        return res