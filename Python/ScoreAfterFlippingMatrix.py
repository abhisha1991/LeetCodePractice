# https://leetcode.com/problems/score-after-flipping-matrix/submissions/
# very similar solution; https://leetcode.com/problems/score-after-flipping-matrix/discuss/143783/Java-two-steps-O(MN)
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m = len(A)
        n = len(A[0])
        A = self.flipRowsWithLeadingZeros(A, m, n)
        print("A AFTER FLIPPING ROWS:" + str(A))
        A = self.flipColsWithManyZeros(A, m, n)
        print("A AFTER FLIPPING COLS:" + str(A))
        return self.sumScore(A, m, n)
    
    def flipColsWithManyZeros(self, A, m, n):
        cols = []
        for j in range(1, n):
            sumcol = 0
            for i in range(m):
                sumcol += A[i][j]
            if sumcol * 2 < m:
                cols.append(j)

        for i in cols:
            A = self.flipCols(A, i, m)
            
        return A
    
    def flipCols(self, A, colnum, row):
        for i in range(row):
            if A[i][colnum] == 0:
                A[i][colnum] = 1
            else:
                A[i][colnum] = 0
                
        return A
            
        
    def flipRowsWithLeadingZeros(self, A, m, n):
        rows = []
        for i in range(m):
            if A[i][0] == 0:
                rows.append(i)
        for i in rows:
            A = self.flipRow(A, i, n)
        
        return A
        
    def flipRow(self, A, rownum, col):
        for j in range(col):
            if A[rownum][j] == 0:
                A[rownum][j] = 1
            else:
                A[rownum][j] = 0
                
        return A
    
    def sumScore(self, A, m, n):
        s = 0
        for i in A:
            j = n-1
            for x in reversed(i):
                s += x * pow(2, n-1-j)
                j -=1
        return s
    