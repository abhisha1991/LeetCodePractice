# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        self.parent = dict()
        
        def helper(n, p):
            if not n:
                return
            
            self.parent[n] = p
            helper(n.left, n)
            helper(n.right, n)
            
        helper(root, root)
        
        if len(nodes) == 1:
            return nodes[0]
        
        # take the first node and find its LCA against every other node
        first = nodes[0]
        
        # populate first node's parent dictionary
        dic = dict()
        while first:
            p = self.parent[first]
            dic[first] = p
            
            if p == first:
                break
            first = p
        
        # finds lca between node n and first node
        def findLca(n):
            while n:
                if n in dic:
                    return n
                
                p = self.parent[n]
                
                if p == n:
                    return None
                
                n = p
        
        # go through all OTHER nodes and populate LCAs list with only unique LCA candidates
        lcas = set()
        for i in range(1, len(nodes)):
            res = findLca(nodes[i])
            lcas.add(res)
        
        # do another traversal to find the global LCA from among the candidates
        # the global LCA will be the FIRST element to be encountered (amongst potential LCAs) as we traverse down the tree
        self.globalLca = None
        def findGlobalLca(node):
            if not node:
                return
            
            if node in lcas and not self.globalLca:
                self.globalLca = node
                return
            
            findGlobalLca(node.left)
            findGlobalLca(node.right)
        
        findGlobalLca(root)
        return self.globalLca