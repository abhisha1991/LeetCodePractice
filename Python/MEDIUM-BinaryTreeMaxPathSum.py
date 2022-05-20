# https://leetcode.com/problems/binary-tree-maximum-path-sum
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.mx = -sys.maxsize
        def helper(node):
            if not node:
                return 0
        
            left = helper(node.left)
            right = helper(node.right)
            
            # return max of 0/left, because we don't want to make things worse by including a -ve 
            # left/right subtree sum to current node's gain
            left = max(0, left)
            right = max(0, right)
            
            # so we're only allowed to split once
            '''
                        1
                      /   \
                     2     3
                          / \
                         4   5
                         
            meaning that we cannot have 2 split points, ie, 2 --> 1 --> 3 --> 4 and 5 cannot be a path
            since we split at both 1 and 3
            
            if we split at 1 only
            2 --> 1 --> 3 --> 4 is one path, sum is 10
            2 --> 1 --> 3 --> 5 is another path, sum is 11
            
            if we split at 3 only
            4 --> 3 --> 5 is the only path, sum is 12
            
            so this is the preferred path since sum is max
            '''
            # so consider each node and assume we're splitting at that node
            # so max gain at this node assuming we're splitting here is going to be 
            # node val + left subtree + right sub tree
            mxgain = node.val + left + right
            self.mx = max(self.mx, mxgain)
            
            # however, when returning at a node level, return node val + max of left or right sub tree
            # why? because for the left/right assignment statements above
            # ie, left = helper(node.left) and right = helper(node.right) we want to only get a non-split result
            '''
            ie, left can be the summation of something like
                        
                    /
                   /
                  /
                  \
                   \
                   /
                       
            but not something like
                        
                    /
                   /\   <--- there is a fork here in the eval of left, which is not allowed, since only 1 split allowed
                  /  \
                  \
                   \
                   /
                       
            '''
            return node.val + max(left, right)
        
        helper(root)
        return self.mx