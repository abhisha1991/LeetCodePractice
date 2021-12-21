# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/ 
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if preorder == None:
            return None
        
        if len(preorder) == 0:
            return TreeNode(None)
        
        return self.helper(preorder)
        
    def helper(self, tree):
        if len(tree) == 0:
            return None
        
        rightTree =[x for x in tree if x > tree[0]]
        leftTree = [x for x in tree if x < tree[0]]
        root = TreeNode(tree[0])
        root.left = self.helper(leftTree)
        root.right = self.helper(rightTree)
        return root
        