# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':        
        # stores key = node, value = parent node
        self.parent = dict()
        
        def helper(node, prt):
            if not node:
                return
            
            self.parent[node] = prt
            helper(node.left, node)
            helper(node.right, node)
        
        # populate parent dictionary
        # remember parent of root == root
        helper(root, root)
        
        # if any of the nodes are not in node to parent dictionary, then there cannot be a lca
        if p not in self.parent or q not in self.parent:
            return None
        
        # parent dictionary for node p
        dicp = dict()
        while p:
            prt = self.parent[p]
            # build parent dictionary for current p
            dicp[p] = prt
            
            # break when we've reached the top of the tree, where the parent of the root == root itself
            if prt == p:
                break
            
            # move up one level and repeat
            p = prt
        
        lca = None
        while q:
            # if q itself is a parent registered in dicp, then q is the lca
            if q in dicp:
                lca = q
                break
                
            prt = self.parent[q]
            
            # first common parent between q and p's lineage is going to be the lca otherwise
            if prt in dicp:
                lca = prt
                break
            
            # in this case, we haven't found an lca since q has also reached the top of the tree
            if prt == q:
                break
            
            # move up one level
            q = prt
            
        
        return lca