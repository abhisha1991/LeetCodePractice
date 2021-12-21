# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Very elegant solution, had thought of this, but couldnt put it properly into code
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(preorder, inorder)

    def helper(self, preorder, inorder):
        if inorder:
            idx = inorder.index(preorder.pop(0))
            # print("preorder element to be searched", inorder[idx])
            root = TreeNode(inorder[idx])
            # print("inorder[0:idx]", inorder[0:idx])
            # print("inorder[idx+1:]", inorder[idx+1:])

            root.left = self.helper(preorder, inorder[0:idx])
            # remember the root.right will be using inorder[idx+1:] and NOT inorder[idx:]
            # why? because idx is the index of root, which has already been considered
            root.right = self.helper(preorder, inorder[idx + 1:])

            return root

s = Solution()
s.buildTree([100,90,50,40,9,5,10,15,45,99,95,96,200,150,250,225],
[5,9,10,15,40,45,50,90,95,96,99,100,150,200,225,250])