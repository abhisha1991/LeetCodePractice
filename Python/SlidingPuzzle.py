# https://leetcode.com/problems/sliding-puzzle/
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        rows = len(board)
        cols = len(board[0])

        def isBoardSolved(grid):
            if grid[0] == [1,2,3] and grid[1] == [4,5,0]:
                return True
            return False
        
        # check if board is already solved
        if isBoardSolved(board):
            return 0
        
        # convert board to a tuple instead of list
        # helps with o(1) lookup in visited set
        b0 = tuple(board[0])
        b1 = tuple(board[1])
        board = (b0, b1)
        
        visited = set()
        
        # 0 is guaranteed to be present in grid,
        # returns pos of 0
        def posZero(grid):
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 0:
                        return (r,c)
        
        directions = [[0,1],[-1,0],[0,-1],[1,0]]
        
        # store in q - current board tuple and number of moves so far as an overall tuple
        q = [(board, 0)]
        while q:
            b, moves = q.pop(0)
            # find pos of 0
            r, c = posZero(b)
            
            if b in visited:
                continue
            
            visited.add(b)
            
            for d in directions:
                newr = r + d[0]
                newc = c + d[1]
                if newr >= 0 and newc >=0 and newr < rows and newc < cols:
                    
                    # swap r,c with newr, newc and check if the resulting board is a 'solved' board
                    # if it is, then return moves+1 - why +1? because we just did a swap which counts as a move
                    
                    # to be able to do swap, we need to re-cast to list because tuples can't be modified
                    newb = [list(b[0]), list(b[1])]
                    tmp = newb[r][c]
                    newb[r][c] = newb[newr][newc]
                    newb[newr][newc] = tmp
                    
                    if isBoardSolved(newb):
                        return moves+1
                    
                    # convert back to a tuple to add to q
                    b0 = tuple(newb[0])
                    b1 = tuple(newb[1])
                    newb = (b0, b1)
                    
                    # board is not solved yet, so add new board state to q
                    q.append((newb, moves+1))
        
        return -1