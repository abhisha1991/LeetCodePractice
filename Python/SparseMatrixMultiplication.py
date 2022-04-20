# https://leetcode.com/problems/sparse-matrix-multiplication/
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # matrix 1
        m = len(mat1)
        k = len(mat1[0])
        
        # matrix 2
        mat2k = len(mat2)
        n = len(mat2[0])
        
        assert(k == mat2k)
        
        # transpose mat 2 to be column major so you can extract a column directly during multiplication
        mat2 = [[mat2[i][j] for i in range(k)] for j in range(n)]
        
        # create a mxn matrix for result
        mul = [[0] * n for i in range(m)]
        
        # multiply 2 vectors
        def doMul(m1, m2):
            res = 0
            v = len(m1)
            for i in range(v):
                res += m1[i] * m2[i]
            return res
        
        '''
        this is the regular way to do multiplication, but doesn't do an optimization
        
        for i in range(m):
            m1 = mat1[i]
            for j in range(n):
                m2 = mat2[j]
                mul[i][j] = doMul(m1, m2)
        '''
        
        # this is the optimization
        for row in range(m):
            m1 = mat1[row]
            
            # length of m1 and m2 should be same, that is what x index is tracking
            for x in range(len(m1)):
                # this is the critical optimization
                # if a given row cell is 0, then we can skip its col cell evaluation
                # note mul is initialized with 0, so it would be naturally 0, so addition is not affected
                '''
                1 0 1    1 1  --> imagine this multiplication (2x3) (3x2) = 2x2
                1 1 1   #1 1#     2 2
                         1 1      3 3
                
                we are saying that for row 1, for index x = 1, value is 0, 
                so we're skipping the 1s that are tagged with # 
                '''
                if m1[x] != 0:
                    for col in range(n):
                        m2 = mat2[col]
                        
                        mul[row][col] += m1[x] * m2[x]
                        
        return mul