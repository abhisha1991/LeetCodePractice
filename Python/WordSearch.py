# https://leetcode.com/problems/word-search
# standard backtracking
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        rows = len(board)
        cols = len(board[0])
        visit = set()
        
        def dfs(r, c, idx):
            # out of bounds
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False
            
            # cannot visit already visited cell
            if (r,c) in visit:
                return False
                
            # we have overshot the index 
            if idx >= len(word):
                return False
            
            # char is not the same, no match
            if word[idx] != board[r][c]:
                return False
            
            if idx == len(word)-1:
                return True
            
            # so now we know that we have a unique path
            # so add it to visited so you dont visit again in the next run of dfs
            visit.add((r,c))
            
            for d in directions:
                if dfs(r+d[0], c+d[1], idx+1):
                    return True
            
            # clean up after yourself, since you couldn't find
            visit.remove((r,c))
            return False
        
        # go through every pos of the board
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False