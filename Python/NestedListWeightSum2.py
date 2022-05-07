# https://leetcode.com/problems/nested-list-weight-sum-ii
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
        self.nums = []
        
    # this does a single pass of dfs
    '''
    we need to find sum(A_i * Weight_i)
    this can be written as sum(A_i * {maxDepth - depth_i + 1})
    this can be written as sum(A_i * (maxDepth + 1) - A_i * (depth_i))
    this can be written as sum(A_i * (maxDepth + 1)) - sum(A_i * (depth_i))
    
    this can be written as (maxDepth+1) * sum(A_i) - sum(A_i * depth_i)
                           |_____________________|   |_______________|
                                PART A                   PART B
                           
    by re-arranging like this, we can find maxDepth for part A and part B together in a single dfs pass
    '''
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        self.helperOptimal(nestedList, 1)
        ans = (self.maxD+1) * sum(self.nums) - self.res
        print(f"maxD is {self.maxD}")
        print(f"nums is {self.nums}")
        print(f"res is {self.res}")
        
        return ans
    
    def helperOptimal(self, nl, depth):
        for element in nl:
            if element.isInteger():
                e = element.getInteger()
                # part A
                self.maxD = max(self.maxD, depth)
                self.nums.append(e)
                # part B
                self.res += depth * e
            else:
                self.helperOptimal(element.getList(), depth+1)
    
    # this does 2 passes of dfs, so its still o(n) but we're doing 2 passes
    # why o(n)? because we're doing one pass to calculate max depth, which takes o(n)
    # and another pass to do the result calculation, which also takes o(n)
    # this passes all test cases, but is not "elegant"
    def depthSumInverse2(self, nestedList: List[NestedInteger]) -> int:
        self.helperMaxD(nestedList, 1)
        self.helper(nestedList, 1)
        return self.res
    
    def helper(self, nl, depth):
        for element in nl:
            if element.isInteger():
                # this is the weight we're supposed to calculate, weight = max depth - curr depth + 1
                self.res += (self.maxD - depth + 1) * element.getInteger()
            else:
                self.helper(element.getList(), depth+1)
    
    def helperMaxD(self, nl, depth):
        for element in nl:
            if element.isInteger():
                self.maxD = max(self.maxD, depth)
            else:
                self.helperMaxD(element.getList(), depth+1)