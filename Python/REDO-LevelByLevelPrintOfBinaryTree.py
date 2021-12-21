# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# https://www.youtube.com/watch?v=7uG0gLDbhsI&t=1s
from collections import defaultdict


class Solution:
    def __init__(self):
        self.q = list()
        self.res = defaultdict()
        self.level = 0

    def levelOrder(self, root):
        if root is None:
            return []
        self.q.append(root)
        self.q.append(None)
        self.levelOrderHelper(root)
        ans = []
        for i in range(0, self.level):
            ans.append(self.res[i])
        return ans

    def levelOrderHelper(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            self.level += 1
            print("Reached level", self.level)
            self.q.append(None)
            self.q = self.q[1:]
            return

        while len(self.q) > 0:
            first = self.q[0]
            if first is None:
                self.levelOrderHelper(first)
            else:
                if first.left != None:
                    self.q.append(first.left)
                if first.right != None:
                    self.q.append(first.right)

                print("Inserting level-value", self.level, first.val)
                if self.level not in self.res.keys():
                    self.res[self.level] = []

                self.res[self.level].append(first.val)
                self.q = self.q[1:]
                self.levelOrderHelper(first)
            if len(self.q) is 1 and self.q[0] == None:
                break
