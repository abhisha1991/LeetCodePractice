# https://leetcode.com/problems/leftmost-column-with-at-least-a-one
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dims = binaryMatrix.dimensions()
        rows = dims[0]
        cols = dims[1]
        
        self.res = sys.maxsize
        def helper(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            p = binaryMatrix.get(r, c)
            if p == 0:
                helper(r+1, c)
            else:
                self.res = min(self.res, c)
                helper(r, c-1)
        
        '''
         Imagine there is a pointer p(x, y) starting from top right corner. 
         p can only move left or down. 
         If the value at p is 0, move down. 
         If the value at p is 1, move left.

         Time complexity is O(M+N) in worse case, space is O(1)
        '''
        
        helper(0, cols-1)
        if self.res == sys.maxsize:
            return -1
        
        return self.res