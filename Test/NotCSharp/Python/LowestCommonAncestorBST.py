# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        # we dont know whether p is bigger or q, so we need to check both conditions
        if (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
            return root
        if p.val <= root.val and q.val <= root.val:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = None # no need to evaluate RHS as root is bigger than both p,q
        if p.val >= root.val and q.val >= root.val:
            right = self.lowestCommonAncestor(root.right, p, q)
            left = None # no need to evaluate LHS as root is smaller than both p,q
        if left and right: return root
        if not left: return right
        if not right: return left
        return None