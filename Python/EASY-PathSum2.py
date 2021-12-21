# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/path-sum-ii/submissions/
class Solution(object):
    def __init__(self):
        self.ans = []
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.helper(root, sum, list())
        return self.ans
    
    def helper(self, root, sum, path):
        if not root:
            return
        
        if sum - root.val == 0 and not root.left and not root.right:
            self.ans.append(list(path + [root.val]))
            
        self.helper(root.left, sum-root.val, path + [root.val])
        self.helper(root.right, sum-root.val, path + [root.val])