# https://leetcode.com/problems/find-leaves-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
        self.visited = set()
        
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        while root:
            self.res.append([])
            self.helper(root)
            if root.left == None and root.right == None:
                break
        
        return self.res
    
    # LRN - do post order traversal
    # why? because we want LR to be displayed in the list before the node itself
    def helper(self, root):
        if not root:
            return

        # if we have already visited the root's left, then mark root's left
        # as None so that root can potentially become a leaf and be evaluated next
        if root.left and root.left in self.visited:
            root.left = None
        else:
            self.helper(root.left)
        
        # if we have already visited the root's right, then mark root's right
        # as None so that root can potentially become a leaf and be evaluated next
        if root.right and root.right in self.visited:
            root.right = None
        else:
            self.helper(root.right)
        
        # if root is a leaf, add to result and add to visited
        # why add to visited? so we don't evaluate it next time and we can use the fact that 
        # this node is visited, to enable the parent to become a future leaf (see above logic)
        if root.right == None and root.left == None:
            self.res[-1].append(root.val)
            self.visited.add(root)