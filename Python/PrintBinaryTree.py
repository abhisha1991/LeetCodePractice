# https://leetcode.com/problems/print-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        self.rows = 0
        self.cols = 0
        
        if not root:
            return []
        
        def getHeight(node, r, c):
            if not node:
                return
            
            self.rows = max(self.rows, r)
            
            getHeight(node.left, r+1, c-1)
            getHeight(node.right, r+1, c+1)
        
        getHeight(root, 0, 0)
        self.cols = 2**(self.rows+1)-1
        
        #print(f"rows are {self.rows} and cols are {self.cols}")
        self.mat = [[''] * self.cols for x in range(self.rows+1)]
        
        def traverse(node, row, l, r):
            if not node:
                return
            
            mid = int((l+r)/2)
            self.mat[row][mid] = str(node.val)
            traverse(node.left, row+1, l, mid-1)
            traverse(node.right, row+1, mid+1, r)
            
            
        traverse(root, 0, 0, self.cols-1)
        return self.mat