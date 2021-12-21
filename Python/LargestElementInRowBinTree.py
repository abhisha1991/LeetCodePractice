# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.dic = dict()
        self.h = 0
        
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.helper(root, 0)
        if len(self.dic) == 0: return []
        
        return [self.dic[i] for i in range(self.h + 1)]
        
        
    def helper(self, root, depth):
        if root == None:
            return
        
        # if key doesnt exist in dic
        if self.dic.get(depth) == None:
            self.dic[depth] = root.val
        # else capture max root val into the dictionary for the given depth
        elif self.dic[depth] < root.val:
            self.dic[depth] = root.val
        
        if self.h < depth:
            self.h = depth
        
        self.helper(root.left, depth+1)
        self.helper(root.right, depth+1)
        