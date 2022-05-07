# https://leetcode.com/problems/nested-list-weight-sum-ii/
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
        self.res = 0
        self.maxD = 0
        
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.helperMaxD(nestedList, 1)
        self.helper(nestedList, 1)
        return self.res
    
    def helper(self, nl, depth):
        for element in nl:
            if element.isInteger():
                # this is the weight sum we're supposed to calculate, where weight = max depth - curr depth + 1
                self.res += (self.maxD - depth + 1) * element.getInteger()
            else:
                self.helper(element.getList(), depth+1)
    
    def helperMaxD(self, nl, depth):
        for element in nl:
            if element.isInteger():
                self.maxD = max(self.maxD, depth)
            else:
                self.helperMaxD(element.getList(), depth+1)