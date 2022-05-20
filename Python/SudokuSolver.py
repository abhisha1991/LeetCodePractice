class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def canPlace(r, c, val):
            row = board[r]
            col = [board[i][c] for i in range(rows)] 
            # if number already in current row or current col, then return false
            if val in row or val in col:
                return False
            
            '''
            gridNum is going to be the index number of the sub grid, ie, 0-8
            
            grid 0 - x
            grid 1 - y
            grid 2 - z
            and so on.... 
        
            x x x y y y z z z 
            x x x y y y z z z
            x x x y y y z z z
            
            a a a b b b c c c
            a a a b b b c c c
            a a a b b b c c c
            
            p p p q q q r r r 
            p p p q q q r r r
            p p p q q q r r r
            
            notice that a grid number can be derived from current row/col idx, for example, r = 4, c = 5
            should belong to grid 4, ie, elements with 'b'
            so (4/3) x 3 + 5/3 = 1 x 3 + 1 = 4
            
            and using the current row/col we can find out the top left/bottom right cell in that grid
            '''
            
            gridNum = int(r/3) * 3 + int(c/3)
            startRow = int(gridNum / 3) * 3
            startCol = int(gridNum % 3) * 3
            endRow = startRow + 2
            endCol = startCol + 2
            
            # go through grid and see if number is already present
            for i in range(startRow, endRow+1):
                for j in range(startCol, endCol+1):
                    if board[i][j] == val:
                        return False
            
            return True
        
        rows = len(board)
        cols = len(board[0])
        arr = range(1, 10)
        visit = set()
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        
        def solve(r, c):          
            # we will go row by row, so when we reach end of col indices, we increment row
            if c == cols:
                r +=1
                c = 0
            
            # if row has reached out of bounds, we have filled all rows, so we have a valid board placement
            if r == rows:
                return True
            
            # if we already have a number present there, we try to move to the next cell
            if board[r][c] != '.':
                return solve(r, c+1)
            
            # otherwise, current (r,c) is a '.', so check if we can place a number 'n' there
            for n in arr:
                if canPlace(r, c, str(n)):
                    # replace that current '.' with n
                    board[r][c] = str(n)
                    # if we can solve the next cell succesfully, return true
                    if solve(r, c+1):
                        return True
                    
                    # bactrack if we couldn't place in the next cell
                    # and try next 'n' in arr
                    board[r][c] = '.'
            
            return False
        
        
        solve(0, 0)
        return board