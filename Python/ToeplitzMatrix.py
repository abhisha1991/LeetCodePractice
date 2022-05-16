# https://leetcode.com/problems/toeplitz-matrix 
class Solution:
    def isToeplitzMatrix(self, matrix):
        groups = {}
        # abs(row-col) is constant for diagonal elements
        # so we can group by this property and store values in a dictionary
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                
                elif groups[r-c] != val:
                    return False
        return True
    
    # also accepted, but slightly harder to follow 
    # here, we are just going down all diagonal elements
    # first, starting from col end to col 0, then starting from row 1 to row end
    def isToeplitzMatrix2(self, matrix: List[List[int]]) -> bool:        
        rows = len(matrix)
        cols = len(matrix[0])
        
        if rows == 1 or cols == 1:
            return True
        
        # start from right end, going down anti diagonal
        # and keep moving one col left and doing the same
        k = 0
        while k < cols:
            i = 0
            j = cols-1-k   
            arr = []
            while j < cols and i < rows:
                if arr and arr[-1] != matrix[i][j]:
                    return False
                
                arr.append(matrix[i][j])
                i +=1
                j +=1
            k +=1
        
        # start from row 1, going down anti diagonal
        # and keep moving one row down and doing the same
        # notice row 0 was already parsed above when col 0 iteration was run
        k = 1
        while k < rows:
            i = k
            j = 0
            arr = []
            while j < cols and i < rows:
                if arr and arr[-1] != matrix[i][j]:
                    return False
                
                arr.append(matrix[i][j])
                i +=1
                j +=1
            k +=1
        
        return True