# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/maximum-binary-tree/ 
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        return self.constructTree(nums)
    
    def constructTree(self, nums):
        if len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        maxnum = max(nums)
        idx = nums.index(maxnum)
        left = nums[0:idx]
        right = nums[idx+1:]
        tree = TreeNode(maxnum)
        tree.left = self.constructTree(left)
        tree.right = self.constructTree(right)
        return tree