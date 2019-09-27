#https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        lst = []
        if not root:
            return []
        node = [root]

        while node:
            curr_node = node.pop()
            lst.append(curr_node.val)
            for i in curr_node.children:
                node.append(i)
        return lst[::-1]
        
