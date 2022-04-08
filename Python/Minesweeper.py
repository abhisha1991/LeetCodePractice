# https://leetcode.com/problems/minesweeper/
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        a = click[0]
        b = click[1]
        rows = len(board)
        cols = len(board[0])
        
        directions = [[0,1],[1,0],[1,1],[-1,-1],[-1,0],[0,-1],[1,-1],[-1,1]]
        
        def outOfBounds(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return True
            return False

        def getNumMines(r, c):
            num = []
            for d in directions:
                newr = r + d[0]
                newc = c + d[1]
                if not outOfBounds(newr, newc) and board[newr][newc] == 'M':
                    num.append(1)
            
            return sum(num)
        
        if outOfBounds(a, b):
            return board
        
        if board[a][b] == 'M':
            board[a][b] = 'X'
            
        elif board[a][b] == 'B':
            return board
        
        elif board[a][b].isdigit():
            return board
        
        # must be E
        else:
            mines = getNumMines(a, b)
            if mines > 0:
                board[a][b] = str(mines)
            else:
                # if there are no immediate mines in vicinity
                # mark that pos as 0, ie, "B"
                board[a][b] = 'B'
                # look into its neighbors
                for d in directions:
                    newr = a + d[0]
                    newc = b + d[1]
                    # remember to "click" on newr, newc and not on the original click pos
                    self.updateBoard(board, [newr, newc])
                        
        return board