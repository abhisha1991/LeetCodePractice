# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dic = defaultdict(list)
        self.minCol = sys.maxsize
        self.maxCol = -sys.maxsize
        
        # essentially we're doing a tree traversal while keeping track of the col and depth info
        def traverse(node, col, depth):
            if not node:
                return
            
            # notice that default dict list was a good choice
            # why? because at the same (col,depth) combo, we can have multiple elements

            '''
                             1
                           /   \
                          2     3
                        /  \   /
                       6    4 5

            here elements 4,5 both have depth = 2 and col = 0
            so self.dic[(0,2)] = [4,5]

            notice that we also want to store the key of the dic as (col,depth) and not (depth,col)
            why? because when we sort the dic keys, we'll have elments with least col show up first, and for same col, we'll have increasing depth sort order
            we want least col to show up first since that's the order in which we want to add to res
            '''
            self.dic[(col, depth)].append(node.val)
            self.minCol = min(self.minCol, col)
            self.maxCol = max(self.maxCol, col)
            
            # left has col-1, right has col+1 but depth keeps increasing since we're going deeper in the tree
            traverse(node.left, col-1, depth+1)
            traverse(node.right, col+1, depth+1)
            
        
        traverse(root, 0, 0)
        res = []
        
        # sort by (col, depth)
        keys = sorted(self.dic.keys())
        k = 0
        
        c = self.minCol
        while c <= self.maxCol:
            # add a new list per column
            res.append([])
            tmp = []
            # as long as columns match in an element in keys vs current column
            # add the node values (which are contained in self.dic) to a tmp list
            while k < len(keys) and keys[k][0] == c:
                # notice we're using extend since self.dic[x] can be a list
                # notice that since we sorted keys before, it has been sorted by increasing depth for the same col
                # which is the order in which we want to insert to tmp
                tmp.extend(self.dic[keys[k]])
                k +=1
            
            # assign tmp to that new list we had created at the column level
            res[-1] = tmp
            # increase col number
            c +=1
        

        return res