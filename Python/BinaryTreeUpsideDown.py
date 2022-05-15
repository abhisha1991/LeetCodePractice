# https://leetcode.com/problems/binary-tree-upside-down/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
                1
               / \
              2   3
             / \
            4   5
        
        we can ignore the right tree part and just look at the left tree for a second
                
                1
               /
              2   
             / 
            4
        
        we maintain the cur, prev and nxt pointers for this left sub tree
        for the right sub tree, we maintain a ptr called lastRight
        
        KEY INSIGHT
        if we think about this, the left bottom most node will be the new tree root after rotation
        also, the right side of the tree (3,5) and all their sub trees (if any) will NOT change
        
        essentially, we need to reverse this 'singly linked list' (left sub tree) and return the new root, ie, 4
        while also ensuring that we have a ptr to the right trees from this left sub tree 'singly linked list'
        
        '''
        if not root or not root.left:
            return root
        
        cur = root
        nxt = None
        prev = None
        lastRight = None

        # evaluate this for node 2 as cur in the tree above
        while cur:
            # 4 becomes nxt
            nxt = cur.left

            # 2.left = 3 (from the previous iteration)
            cur.left = lastRight
            # new lastRight should become 2.right, ie, 5 (which will be linked in the next iteration)
            # when we do 4.left = 5
            lastRight = cur.right
            
            # we need to do 2.right = 1 (ie, point backward)
            cur.right = prev
            # make 2 as the now 'prev', so that we can later do 4.right = 2 in the next iteration
            prev = cur
            # make cur as 4
            cur = nxt 
        
        # in the end, cur will be None (that's how we broke out of the while loop)
        # so prev will hold the last valid node, ie, 4, ie, our new root!
        return prev