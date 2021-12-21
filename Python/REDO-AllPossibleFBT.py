#https://leetcode.com/problems/all-possible-full-binary-trees
# note that all even numbers cannot have FBTs
# read solution explanation from leetcode website

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    dic = {0:[], 1:[TreeNode(0)]}
    
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N not in Solution.dic.keys():
            ans = []
            for x in range(0, N):
                y = N-1-x # why -1? because we are creating a root node with 1 "0" value already
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        root = TreeNode(0)
                        root.left = left # left has x number of nodes with 0 value
                        root.right = right # right has y number of nodes with 0 value
                        # keep in mind, x + y = N-1, the last node is coming from the 'root' node by doing TreeNode(0)
                        # so all in all, we have x + y + 1 = N nodes for this tree with parent node = root
                        ans.append(root) # ans has a list of all trees with N nodes
            Solution.dic[N] = ans
        return Solution.dic[N]

# My first solution - didnt work, but was worth a try - needed to have parent of trees captured somewhere to append to the final answer. "Parent" was designed to do that.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    treelist = []
    
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N % 2 == 0:
            return []
    
        if (N ==1):
            return [TreeNode(0)]
        
        t = TreeNode(0)
        parent = t
        self.createFBT(N-1, t, parent)
        return Solution.treelist
    
    def createFBT(self, n, t, parent):
        if n < 0:
            return
        if n == 0:
            Solution.treelist.append(parent)
            return
        if n == 1:
            return
        # n is atleast 2
        # so create 2 new nodes
        c1 = TreeNode(0)
        c2 = TreeNode(0)
        # add to left and right
        t.left = c1
        t.right = c2
        self.createFBT(n-2, t.left, parent)
        self.createFBT(n-2, t.right, parent)
        