# https://leetcode.com/problems/surrounded-regions/
# the smarter way to do dfs is to start at the border cells, start with 'O' there
# if we do dfs on a border cell 'O' and move inwards to other 'O' cells, we know that these other 'O' cells will NOT be converted to 'X'
# since these cells are all connected to the border, so we can mark these cells as '#' say
# do this for all border cell dfs
# once this is complete, all remaining 'O' cells are not connected to border, so we can mark them as 'X'
# revert the border connected 'O' cells (which were marked '#') back to 'O'

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        v = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False
            
            if (r,c) in v:
                return True
            
            if board[r][c] == 'X':
                return True
            
            v.add((r,c))
            
            for d in directions:
                arr.append(dfs(r + d[0], c + d[1]))
            
            return True
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    # reset the arr and visited set every time we're going for dfs
                    v = set()
                    arr = []
                    
                    dfs(i, j)
                    
                    if all(arr):
                        # make everything visited so far as X
                        for rc in v:
                            board[rc[0]][rc[1]] = 'X'