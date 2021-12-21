# https://leetcode.com/problems/minimum-falling-path-sum
# time limit is exceeding with the solution below, so instead read this: https://leetcode.com/problems/minimum-falling-path-sum/solution/
class Solution(object):
    def __init__(self):
        self.ans = []
    
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for x in range(len(A[0])):
            self.minsum(A, 0, x, 0)
        
        print(self.ans)
        return min(self.ans)
        
    
    def isValidIndex(self,i,j,A):
        if i < len(A) and i >=0 and j >=0 and j < len(A[0]):
            return True
        return False
    
    def minsum(self, A, i, j, sumsofar):
        if self.isValidIndex(i, j, A) == False:
            return sumsofar

        sumsofar += A[i][j]
        i +=1
        ms = min(self.minsum(A, i, j, sumsofar), self.minsum(A, i, j-1, sumsofar), self.minsum(A, i, j+1, sumsofar))
        
        if i == len(A):
            self.ans.append(ms)
            return ms
        
        return sumsofar