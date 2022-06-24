# https://leetcode.com/problems/balance-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.arr = []
        
        def helper(node):
            if not node:
                return 
            
            helper(node.left)
            self.arr.append(node)
            helper(node.right)
        
        helper(root)
        # now we have the tree in arr
        # so reconstruct the tree from the arr
        
        '''
                    [1,2,3,4,5]
                    
                         3
                        / \ 
                       2   4
                      /     \ 
                     1       5
        
        mid point is root, left part of arr is left sub tree, right part of arr is right sub tree
        '''
        def makeTree(low, high):
            if low > high:
                return
            
            mid = (low + high)//2
            root = self.arr[mid]
            root.left = makeTree(low, mid-1)
            root.right = makeTree(mid+1, high)
            return root
        
        return makeTree(0, len(self.arr)-1)