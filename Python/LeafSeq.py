# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/leaf-similar-trees/submissions/

class Solution(object):
    def __init__(self):
        self.res1 = []
        self.res2 = []
        
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.leafseq(root1, True)
        self.leafseq(root2, False)
        return self.res1 == self.res2
        
    def leafseq(self, root, primary):
        if not root:
            return
        
        # do inorder traversal, LNR
        # if node is a leaf, then add it to sequence
        self.leafseq(root.left, primary)
        
        if root.left == None and root.right == None:
            if primary:
                self.res1.append(root.val)
            else:
                self.res2.append(root.val)
            
        self.leafseq(root.right, primary)