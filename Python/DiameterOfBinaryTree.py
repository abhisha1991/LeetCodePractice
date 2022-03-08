# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = []
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameterHelper(root)
        return max(self.d)
    
    def diameterHelper(self, root):
        if not root:
            return 0
        
        left = self.diameterHelper(root.left)
        right = self.diameterHelper(root.right)
        
        self.d.append(left + right)
        return max(left, right) +1

'''
The key observation to make is: the longest path has to be between two leaf nodes. We can prove this with contradiction. 
Imagine that we have found the longest path, and it is not between two leaf nodes. 
We can extend that path by 1, by adding the child node of one of the end nodes (as at least one must have a child, given that they aren't both leaves). 
This contradicts the fact that our path is the longest path. Therefore, the longest path must be between two leaf nodes.

Moreover, we know that in a tree, nodes are only connected with their parent node and 2 children. 
Therefore we know that the longest path in the tree would consist of a node, its longest left branch, and its longest right branch. 
So, our algorithm to solve this problem will find the node where the sum of its longest left and right branches is maximized. 
This would hint at us to apply Depth-first search (DFS) to count each node's branch lengths, 
because it would allow us to dive deep into the leaves first, and then start counting the edges upwards.
'''