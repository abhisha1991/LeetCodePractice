# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # uses o(1) space. This is Morris Traversal: https://www.youtube.com/watch?v=wGXB9OWhPTg
    # this modifies the tree itself temporarily, 
    # by setting links to from predecessor (inorder child) to its backtracked root
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root
        while cur is not None:
            # if left sub tree doesn't exist (LNR) ==> L is None, 
            # so visit "cur" and move to right subtree 
            if cur.left is None:
                res.append(cur.val)
                cur = cur.right
            else:
                # in inorder -- we are getting the "predecessor"
                # ie, the child node of current who precedes cur in the traversal
                # once we have this predecessor, we are establishing a link between it and the parent cur
                # this allows us to do the backtracking that is done by the internal stack in the recursive case

                # start with left sub tree and keep moving right, ie, find right most child in the left sub tree
                pre = cur.left
                while pre.right != cur and pre.right is not None:
                    pre = pre.right
                
                # which of the conditions broke the above while loop?
                if pre.right == None:
                    # this is the link from the predecessor (child node)
                    # connecting back to the parent root (cur)
                    # this is what helps us "back track"
                    pre.right = cur
                    cur = cur.left
                
                # left side of cur was already visited
                # this is the part where we're moving to "R" in LNR
                elif pre.right == cur:
                    # reset the back link we temporarily established again to none
                    # this helps keep the tree "unmodified"
                    pre.right = None
                    
                    res.append(cur.val)
                    cur = cur.right
        return res
    
    # also using Morris traversal, the ONLY difference between pre and inorder is that 
    # we enter into "res" at a different place
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root
        while cur is not None:
            if cur.left is None:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right != cur and pre.right is not None:
                    pre = pre.right
                
                if pre.right == None:
                    pre.right = cur
                    # THIS IS THE ONLY DIFFERENCE
                    res.append(cur.val)
                    cur = cur.left
                
                elif pre.right == cur:
                    pre.right = None
                    cur = cur.right
        return res

    # uses o(n) space since we use internal stack in memory during recursion
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def helper(r):
            if not r:
                return
            
            helper(r.left)
            res.append(r.val)
            helper(r.right)
            
        helper(root)
        return res
        
        