# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.graph = defaultdict(list)
        if not root:
            return None
        
        self.start = None
        self.end = None
        
        def traversal(node, parent):
            if not node:
                return
            
            self.graph[node] = [('U', parent), ('L', node.left), ('R', node.right)]
            if node.val == startValue:
                self.start = node
            if node.val == destValue:
                self.end = node
            
            traversal(node.left, node)
            traversal(node.right, node)
        
        traversal(root, None)
        
        # now do bfs to get shortest path from source to dest
        # q stores current element and path so far as a tuple
        q = [(self.start, '')]
        visited = set()
        while q:
            first, path = q.pop(0)
            
            visited.add(first)
            if first == self.end:
                return path
            
            for nbor in self.graph[first]:
                direction = nbor[0]
                node = nbor[1]
                if node not in visited:
                    q.append((node, path + direction))
        
        return ''