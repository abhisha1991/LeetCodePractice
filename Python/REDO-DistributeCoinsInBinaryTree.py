# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/distribute-coins-in-binary-tree/solution/
# https://leetcode.com/problems/distribute-coins-in-binary-tree/discuss/221939/C%2B%2B-with-picture-post-order-traversal
class Solution(object):
    moves = 0
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Solution.moves = 0
        self.postorder(root)
        return Solution.moves
        
    def postorder(self, root):
        if root == None:
            return 0
        
        l = self.postorder(root.left)
        r = self.postorder(root.right)
        # the below will give us the total children excess / defecit sum which needs to be distributed from the current node to the children
        Solution.moves += abs(l) + abs(r)
        # we are considering how many coins we have + how many are in excess / need in left and right - 1
        # why -1? because we need to assign the current node (us) 1 coin as well
        return (root.val + l + r - 1)
        