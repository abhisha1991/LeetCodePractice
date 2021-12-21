# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            # if tree is Null, difference is 0
            return 0
        # ans is an array with 3 elements, 
        # 0th element = min element of tree up till root
        # 1st element = max element of tree up till root
        # 2nd element = largest difference found between any parent and any child, up till root (root included)
        ans = self.getMinMaxCurrDiff(root)
        # so ans[2] will contain the answer we are looking for
        return ans[2]
    
    def getMinMaxCurrDiff(self, root):
        # curr min and curr max are initially set to the current node
        currMin = root.val
        currMax = root.val
        currDiff = 0
        # if the node is a leaf, then return with default values
        if root.left == None and root.right == None:
            return [currMin, currMax, currDiff]
        
        if root.left != None:
            # ansleft = the min element of the left tree, max element in the left tree and largest difference in the left tree
            ansleft = self.getMinMaxCurrDiff(root.left)
            currMin = min(currMin, ansleft[0])
            currMax = max(currMax, ansleft[1])
            # there are 3 values to consider to update the currDiff, get the lowest diff till now
            option1diff = abs(root.val - ansleft[0])
            option2diff = abs(root.val - ansleft[1])
            option3diff = max(currDiff, ansleft[2])
            currDiff = max(option1diff, option2diff, option3diff)
        
        # do the same for the right tree
        if root.right != None:
            ansright = self.getMinMaxCurrDiff(root.right)
            currMin = min(currMin, ansright[0])
            currMax = max(currMax, ansright[1])
            option1diff = abs(root.val - ansright[0])
            option2diff = abs(root.val - ansright[1])
            option3diff = max(currDiff, ansright[2])
            currDiff = max(option1diff, option2diff, option3diff)
        
        # return the 3 values for the present node
        return [currMin, currMax, currDiff]

'''
[8,3,10,1,6,null,14,null,null,4,7,13]
            
            8
           / \
          3  10
         /\     \
        1  6     14
          / \    /
         4   7  13

4 returns [4,4,0]
7 returns [7,7,0]
6 returns [4,7,2] after looking at [4,4,0] and [7,7,0]. To find out currDiff, it compares (0,0,abs(6-4),abs(6-4),abs(6-7),abs(6-7))
1 returns [1,1,0] 
3 returns [1,7,4] after looking at [4,7,2] and [1,1,0]. To find out currDiff, it compares (2,0,abs(3-4),abs(3-1),abs(3-7),abs(3-1))
13 returns [13,13,0]

'''
            