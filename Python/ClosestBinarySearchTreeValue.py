# https://leetcode.com/problems/closest-binary-search-tree-value
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import bisect
class Solution:
    # this is an o(logn) solution since you're getting the closest value as you walk down the tree
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if not root:
            return None
        
        closest = root.val
        while root:
            if abs(root.val - target) < abs(closest - target):
                closest = root.val
            
            if target < root.val:
                root = root.left
                
            else:
                root = root.right
            
        return closest

    # this is an o(n) solution since we're having to construct the binary search tree into an arr
    def closestValue2(self, root: Optional[TreeNode], target: float) -> int:
        self.arr = []
        
        def helper(node):
            if not node:
                return

            # always remember that inorder of a bst gives you sorted arr
            helper(node.left)
            self.arr.append(node.val)
            helper(node.right)
        
        
        helper(root)
        left = bisect.bisect_left(self.arr, target)
        right = bisect.bisect_right(self.arr, target)
        
        # the target number exactly exists in arr
        if left != right:
            return self.arr[left]
        
        # edge case, target number is smaller than all other numbers
        if left == 0:
            return self.arr[left]
        
        # edge case, target number is larger than all other numbers
        if left == len(self.arr):
            return self.arr[left-1]
        
        # regular case, we need to check left-1 and left
        # see which one has a lesser abs diff from target and return that num
        if abs(target - self.arr[left-1]) < abs(target - self.arr[left]):
            return self.arr[left-1]
        return self.arr[left]