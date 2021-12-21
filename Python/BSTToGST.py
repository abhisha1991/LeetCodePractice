# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/submissions/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.s = 0
        
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.revinorder(root)
        return root
    
    def revinorder(self, root):
        if root == None:
            return
        
        # reverse inorder because we want to get the sum for right elements of the root
        # inorder is LNR, so reverse will be RNL
        self.revinorder(root.right)
        print("evaluating root:" +  str(root.val))
        # self.s will hold all the sums of the right of the root
        self.s += root.val
        root.val = self.s
        print("sum so far:" + str(self.s))
        print("new root:" +  str(root.val))
        self.revinorder(root.left)
        