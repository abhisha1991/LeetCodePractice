# https://leetcode.com/problems/clone-graph/
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # dic has key = old node, value = node node that is the copy of this old node
        dic = dict()
        
        if not node:
            return None
        
        def dfs(n):
            if n in dic:
                return
            
            # store copy for the old node as value
            dic[n] = Node(n.val)
            
            for nbor in n.neighbors:
                dfs(nbor)
        
        dfs(node)
        
        for old,new in dic.items():
            # get neighbors from the old node
            nbors = old.neighbors
            # assign the neighbors of the new node as a list
            # where the items of the list are going to be dic[oldNode]
            new.neighbors = [dic[n] for n in nbors]
            
        
        return dic[node]