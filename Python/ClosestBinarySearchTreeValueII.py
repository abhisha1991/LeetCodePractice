# https://leetcode.com/problems/closest-binary-search-tree-value-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import bisect
class Solution:
    def __init__(self):
        self.arr = []
        
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        if not root:
            return []
        
        # get all elements from tree and sort them
        self.helper(root)
        self.arr.sort()
        
        res = []
        
        # bisect.bisect_left returns the leftmost place in the sorted list to insert the given element. 
        # bisect.bisect_right returns the rightmost place in the sorted list to insert the given element
        # [1, 5, 8, 15], 
        # say you're inserting 10, then both bisects will give index 3
        # say you're inserting 8, then bisect left gives 2, bisect right gives 3
        
        i = bisect.bisect_left(self.arr, target) 
        j = bisect.bisect_right(self.arr, target)
        if i == j:
            # make i be one less
            i -= 1
        
        while k > 0 and i >=0 and j < len(self.arr):
            # take the abs diff from this target to what is in ith and jth pos
            # whoever is less, insert that to res
            if abs(self.arr[i] - target) <= abs(self.arr[j] - target):
                res.append(self.arr[i])
                i -=1
            else:
                res.append(self.arr[j])
                j +=1
            k -=1
            
        # if j overflowed but we're still left with k elements to fill
        while k > 0 and i >=0:
            res.append(self.arr[i])
            i -=1
            k -=1
        # if i overflowed but we're still left with k elements to fill 
        while k > 0 and j < len(self.arr):
            res.append(self.arr[j])
            j +=1
            k -=1
        
        return res
    
    def helper(self, root):
        if not root:
            return
        
        self.arr.append(root.val)
        self.helper(root.left)
        self.helper(root.right)