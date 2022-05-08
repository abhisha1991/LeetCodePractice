# https://www.youtube.com/watch?v=T6E74ypY_tU
# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
import sys
# https://www.youtube.com/watch?v=T6E74ypY_tU
import sys
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # note arr contains only leaf nodes!
        if len(arr) == 0:
            return 0
        
        if len(arr) == 2:
            return arr[0] * arr[1]
        
        # dictionary for memoization
        # consider an array like [6,3,2,4] --> [6|2,3,4], [6,2|3,4], [6,2,3|4] -- these are the ways in which
        # we break this array input in the function to form left and right sub trees
        # notice that in 6|2,3,4 and in 6,2|3,4 we are solving a common problem -- (3,4)
        # so we can memoize!
        # here memoization will contain key = (startIdx, endIdx) of arr
        dic = dict()
        
        # returns a tuple
        # first element contains max leaf node between left and right sub trees
        # second element contains min sum of non leaf nodes from left and right sub trees
        def minCost(l, r, a):
            if l > r:
                # invalid case
                # return neutral leaf node like 1 - why? since this is used to form a product later on
                # product with a number like 1 doesn't change the product
                # sum returned is 0
                return (1, 0)
            
            if l == r:
                # max leaf is just the single element leaf given in range l,r
                # sum of non leaf nodes is 0, since the array doesn't contain non leaf nodes
                return (a[l], 0)
            
            if (l,r) in dic:
                return dic[(l,r)]
            
            i = l
            # current tuple values for l,r
            # minSum is going to contain the min sum for all non leaf nodes in partitions considered between l and r
            # in example, 6,3,2,4 with l=0 and r=4 -- it will be [6|3,2,4], [6,3|2,4], [6,3,2|4]
            # max leaf is the max leaf value in left/right sub tree - in the example, it is 6
            minSum = sys.maxsize
            maxLeaf = None
            
            while i < r:
                l1, c1 = minCost(l, i, a)
                l2, c2 = minCost(i+1, r, a)
                
                # total is sum of non leaf nodes
                # why is this total going to be sum of non leaf nodes?
                
                # because for "parent of leaf nodes", say 12 below we will return something like (6,0), (2,0)
                # since "non-leaf node sum" for a leaf node is 0
                # so we calculate 12 itself as product of max leaf nodes, 6x2
                # at the next level, we calculate 24 as product of max leaf nodes 6x4
                # so total sum of non-leaf nodes at root is = 24 (self = mxleaf1 x mxleaf2) + 12 (c1) + 0 (c2)
                '''
                            24  (minSum = 6 x 4 + 12 + 0, maxLeaf=6)
                           /  \ 
                 (6,12)  12    4 (4,0)
                        /  \
                       6    2 
                     (6,0)  (2,0)
                     
                '''
                total = c1 + c2 + l1 * l2
                if total < minSum:
                    minSum = total
                maxLeaf = max(l1, l2)
                    
                i +=1
            
            dic[(l,r)] = (maxLeaf, minSum)
            return dic[(l,r)]
            
        
        leaf, cost = minCost(0, len(arr)-1, arr)
        return cost