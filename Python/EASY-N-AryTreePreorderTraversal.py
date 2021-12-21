#https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        lst = []
        node = [root]

        while node:
            curr_node = node.pop(0)
            lst.append(curr_node.val)
            for i in curr_node.children[::-1]:
                node.insert(0, i)
        return lst
