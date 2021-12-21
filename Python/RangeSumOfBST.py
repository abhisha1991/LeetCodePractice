# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/range-sum-of-bst/submissions/
class Solution:
    x = 0
        
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        Solution.x = 0
        self.sum_traversal(root, L, R)
        print("x: " + str(Solution.x))
        return Solution.x
    
    def sum_traversal(self, root, L, R):
        if (root == None):
            return Solution.x
        
        if (root.val >= L and root.val <=R):
            Solution.x += root.val
            print("root val is" + str(root.val))
            print("x is " + str(Solution.x))
        
        self.sum_traversal(root.left, L, R)
        self.sum_traversal(root.right, L, R)
        