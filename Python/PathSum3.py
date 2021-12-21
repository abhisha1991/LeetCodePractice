# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/path-sum-iii/
# brute force solution, this is not ideal - worst case O(n*n), when tree is skewed
# average case o(NlogN) - why?
# because, dfs method does o(N) - traverses every node, 
# the logN comes from helper function where we need to traverse from node to leaf which depends on height, ie, logN
class Solution2(object):
    def __init__(self):
        self.count = 0
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.dfs(root, sum)
        return self.count
    
    # traverses through each node
    def dfs(self, root, sum):
        if not root:
            return
        
        # "helper" traverses through each node treating current as the starting point of the path
        # checks if we reach target sum given current node as start of the path
        # if we do, increment self.count
        self.helper(root, sum)
        
        # traverse through other nodes - left and right
        self.dfs(root.left, sum)
        self.dfs(root.right, sum)
    
    def helper(self, root, sum):
        if not root:
            return
        
        if sum - root.val == 0:
            self.count +=1
        
        self.helper(root.left, sum-root.val)
        self.helper(root.right, sum-root.val)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# copied from 
# https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
# need to understand fully - this is an O(n) solution
class Solution(object):
    def __init__(self):
        self.count = 0
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        dic = dict()
        dic[0] = 1
        self.helper(root, 0, sum, dic)
        return self.count
    
    def helper(self, root, currsum, sum, dic):
        if not root:
            return
        
        currsum += root.val
        oldsum = currsum - sum
        self.count += dic.get(oldsum, 0)
        dic[currsum] = dic.get(currsum, 0) + 1
        
        self.helper(root.left, currsum, sum, dic)
        self.helper(root.right, currsum, sum, dic)
        dic[currsum] -=1
        
        