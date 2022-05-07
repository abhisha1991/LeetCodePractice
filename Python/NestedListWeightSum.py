# https://leetcode.com/problems/nested-list-weight-sum
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def __init__(self):
        self.nl = None
        self. res = 0
        
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.nl = nestedList
        self.helper(nestedList, 1)
        return self.res
    
    def helper(self, nl, depth):
        # imagine something like [[1,1], 2, [3,4]]
        '''
        1st element is [1,1] which is a nested integer, so we go into else block and call helper([1,1], 2) with depth 2
            in this dfs call for [1,1] - both elements will unwrap as integers with depth 2, so we just add these to res, 1 x 2 + 1 x 2 = 4
        
        coming out of this dfs call, we evaluate 2nd element, which is 2 -- 
        this is an integer and current depth is 1 (we are now out of 1st dfs, back to parent caller), so res becomes 4 + 2 x 1 = 6

        now evaluate last element, [3,4] which is a nested integer, so go into else block and call helper([3,4], 2) with depth 2
            in this dfs call for [3,4] - both elements will unwrap as integers with depth 2, so we just add these to res, 6 + 3 x 2 + 4 x 2 = 20
        
        return 20
        '''
        for element in nl:
            if element.isInteger():
                self.res += depth * element.getInteger()
            else:
                self.helper(element.getList(), depth+1)