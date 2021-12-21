# https://leetcode.com/problems/find-bottom-left-tree-value/
# the below approach uses dfs - like a preorder traversal.
# typically, people have solved this using bfs, like level order traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.h = 0
        self.ans = None
        
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root, 1)
        return self.ans
        
    def helper(self, root, depth):
        if self.h < depth:
            self.h = depth
            self.ans = root.val
        
        if (root.left):
            # if left is not empty explore left
            self.helper(root.left, depth+1)
        
        if (root.right):
            # if right is not empty, explore right
            self.helper(root.right, depth+1)        

'''
lets pick an example like

         1
        / \
       2   3
      /    /
     4     5

In this case, both 2 and 3 have left children.
In this case, the answer should be 4 as it is the left most.

this is ensured in our solution by 2 things
1. we check if "self.h < depth" --> this means that we are only honoring the first element where our own height is smaller than the proposed depth. Both elements 4 and 5 have a depth of 3, but once we have processed element 4, then element 5 will not be processed as we have updated our height to 3
2. this means that we need to ensure that 4 is the element that is evaluated first --> for element 4 to be evaluated first, we need to do preorder traversal (NLR)
'''

'''
BFS solution
https://leetcode.com/problems/find-bottom-left-tree-value/discuss/98779/Right-to-Left-BFS-(Python-%2B-Java)
try tracing the simple queue logic for the above tree (see java solution)
We want the answer to be 4 again. So we have a queue, such that we insert the root initially
Then we pull that root from the queue (FIFO) and "add its right element, then left element"
q = [1]
q = [3,2] # right element then left element
q = [2,5] # 3 doesnt have right element
q = [5,4] # 2 doesnt have right element
q = [4] # 5 doesnt have any children
q = [] # now root has value of 4
last root is our answer!
By placing right element, then left element, we ensure that the last elment in the queue is the left most leaf
why was 5 inserted before 4 to begin with? because the right tree is evaluated first because the right child is inserted into q first
'''
