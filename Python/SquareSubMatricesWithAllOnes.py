# https://leetcode.com/problems/count-square-submatrices-with-all-ones
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        squares = [[0] * cols for r in range(rows)]
        total = 0
        # here, square[i][j] is representing the endpoint (bottom right point) of a square
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    # if we're at the first row/col, we cannot make further squares
                    # the only ones we can make are if the number itself is a 1
                    squares[i][j] = matrix[i][j]
                
                # 0 can never be part of a square submatrix
                # so the corresponding square i,j pos will also be 0
                elif matrix[i][j] == 0:
                    pass
                
                else:
                    # matrix i,j is 1
                    '''
                    0  1  1  1     0  1  1  1
                    1  1  1  1 ==> 1  1  2  2
                    0  1  1  1     0  1  2  3

                    this is saying that the number of squares ending at (bottom right) i,j = 1,2 are 2 
                    because it consists of the element 1 by itself and consists of the adjacent ones to its north, west and north west
                    '''
                    squares[i][j] = 1 + min(squares[i-1][j], squares[i][j-1], squares[i-1][j-1])
                
                total += squares[i][j]
        
        return total