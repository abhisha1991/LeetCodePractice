# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii
# the difference between LCA II and LCA III (this one) is that there is a back link given to us between each node and its parent 
# in the node defition itself -- if we see below (self.parent is a property of the Node class)
# so we don't have to explicitly create the parent dictionary, so our life is actually easier in this question
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # parent dictionary for node p
        dicp = dict()
        while p:
            prt = p.parent
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
                
            prt = q.parent
            
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