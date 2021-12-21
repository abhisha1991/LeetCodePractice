# https://leetcode.com/problems/subtree-of-another-tree/submissions/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = False
        
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        self.helper(s, t)
        return self.ans
         
    def helper(self, s, t):
        if not s:
            return
        
        if s.val == t.val:
            ss = s
            tt = t
            if self.treeEqual(ss, tt):
                self.ans = True
                return
        
        self.helper(s.left, t)
        self.helper(s.right, t)
        
    def treeEqual(self, sroot, troot):
        if not sroot and not troot:
            return True
        
        if not sroot or not troot:
            return False
        
        if sroot.val != troot.val:
            return False
        
        return self.treeEqual(sroot.left, troot.left) and \
                self.treeEqual(sroot.right, troot.right)