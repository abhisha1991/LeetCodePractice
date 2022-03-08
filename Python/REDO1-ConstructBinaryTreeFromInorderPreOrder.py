# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeHelper(preorder, inorder)
    
    def buildTreeHelper(self, preOrder, inOrder):
        if len(inOrder) == 0:
            return None
        
        # notice that in pre-order, 0th element is ALWAYS the root (NLR)
        rootval = preOrder.pop(0)
        root = TreeNode(rootval)
        
        # we need to get the split point assuming this root value is present in the inOrder
        # which it always is according to the question
        idx = inOrder.index(root.val)
        
        # for the left part of the tree, we are only allowed to view 0 to idx-1th element of the inorder
        # remember, preOrder here still contains 0th element as root of the left tree
        root.left = self.buildTreeHelper(preOrder, inOrder[0:idx])
        
        # remember the root.right will be using inorder[idx+1:] and NOT inorder[idx:]
        # why? because idx is the index of root, which has already been considered
        # remember, preOrder here still contains 0th element as root of the right tree
        root.right = self.buildTreeHelper(preOrder, inOrder[idx+1:])
        return root

s = Solution()
s.buildTree([100,90,50,40,9,5,10,15,45,99,95,96,200,150,250,225],
[5,9,10,15,40,45,50,90,95,96,99,100,150,200,225,250])