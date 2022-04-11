# https://leetcode.com/problems/range-sum-query-2d-immutable
# https://www.techiedelight.com/calculate-sum-elements-sub-matrix-constant-time/
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.mat = self.preProcess(matrix)
        # print(f"mat is {self.mat}")

    def preProcess(self, matrix):
        # mat contains prefix sum from 0,0 up to that r,c
        # for example, mat[1][1] contains sum of all elements in range 0,0 to 1,1
        # that is, mat[1][1] = matrix[0][0] + matrix[1][0] + matrix[0][1] + matrix[1][1]
        mat = [[0] * self.cols for x in range(self.rows)]
        
        # first row and first col are special
        # store the 0,0 element as is, because there is no left/above col/row
        mat[0][0] = matrix[0][0]
        
        # handle first row, iterate over cols
        for i in range(1, self.cols):
            mat[0][i] = mat[0][i-1] + matrix[0][i]
        
        # handle first col, iterate over rows
        for i in range(1, self.rows):
            mat[i][0] = mat[i-1][0] + matrix[i][0]
        
        # for all remaining rows and cols, calculate prefix sum (pfs)
        # this would be yourself + just above row pfs + just left col pfs
        # remember to subtract the diagonal pfs. Why?
        # you're adding it twice in the the above 2 pfs additions
        for i in range(1, self.rows):
            for j in range(1, self.cols):
                mat[i][j] = matrix[i][j] + mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]
                
        return mat
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.mat:
            return 0
        
        # total sum up to the end row/col
        total = self.mat[row2][col2]
        
        # try this with an example
        '''
        1 2 3     1  3   6
        4 5 6 ==> 5  12  21  
        7 8 9     12 27  45
        
        say you want to get a range 1,1 to 2,2 ==> 5 + 6 + 8 + 9 = 28
        so this will be 45 - 6 - 12 + 1 = 28
        so total = mat[2][2] - mat[0][2] - mat[2][0] + mat[0][0]
        
        this piece is important, observe the if statements 
        observe which elements we're trying to subtract from total

        #1 --> mat[row-1][col2] is top right element prefix sum (just outside of box of interest)
        #2 --> mat[row2][col1-1] is bottom left element prefix sum (just outside box of interest)

        again, if we subtract both these from total, 
        we've subtracted the "common matrix" (which was part of #1 and #2) twice, so we need to add it back, ie, mat[row1-1][col1-1]
        '''
        
        if row1 - 1 >= 0:
            total -= self.mat[row1-1][col2]
        
        if col1 - 1 >= 0:
            total -= self.mat[row2][col1-1]
        
        if row1 - 1 >=0 and col1 - 1 >=0:
            total += self.mat[row1-1][col1-1]
            
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)