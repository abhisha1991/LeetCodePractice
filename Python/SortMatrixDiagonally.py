# https://leetcode.com/problems/sort-the-matrix-diagonally
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:        
        def collectAndSortDiagonalElements(x, y, rows, cols, matrix):
            arr = []
            while y < cols and x < rows:
                arr.append(mat[x][y])
                x +=1
                y +=1
            return sorted(arr)
                
        rows = len(mat)
        cols = len(mat[0])
        if rows <= 1:
            return mat
        
        # column counter
        c = 0
        # uber iteration for going right to left 
        while c < cols:
            # collect elements in arr
            j = cols-1-c
            i = 0
            arr = collectAndSortDiagonalElements(i, j, rows, cols, mat)
            
            # refill arr elements into mat
            j = cols-1-c
            i = 0
            k = 0
            while j < cols and i < rows:
                mat[i][j] = arr[k]
                i +=1
                j +=1
                k +=1
            
            c +=1
        
        # row counter
        r = 0
        # uber iteration for going from row 1 to last row 
        while r < rows:
            # collect elements in arr
            i = r+1 
            j = 0
            arr = collectAndSortDiagonalElements(i, j, rows, cols, mat)
            
            # refill arr elements into mat
            i = r+1
            j = 0
            k = 0
            while j < cols and i < rows:
                mat[i][j] = arr[k]
                i +=1
                j +=1
                k +=1
            
            r +=1
        
        return mat