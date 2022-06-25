# https://leetcode.com/problems/diameter-of-n-ary-tree
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.d = 0
        
        def helper(node):
            if not node:
                return 0
            
            # arr has 2 zeros since we need to access at least 2 elements: arr[0], arr[1]
            # as seen in the diameter calculation below
            # having zeros in arr doesn't make any difference since its a neutral value
            arr = [0, 0]
            for c in node.children:
                arr.append(helper(c))
            
            # sort by reverse, because we want top 2 max depths
            arr.sort(reverse=True)
            
            # arr[0] and arr[1] are the top 2 max depths of all children of this node
            # so diameter is going to be their sum, ie, 2 paths that diverge at this node
            # that are the top 2 deepest, reaching to leaves
            self.d = max(self.d, arr[0] + arr[1])
            
            # return max depth from all chidlren including yourself (the +1 is yourself)
            return 1 + max(arr)
        
        helper(root)
        return self.d