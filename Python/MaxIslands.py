# https://leetcode.com/problems/max-area-of-island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        res = [0]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        def dfs(r,c):
            # if out of bounds
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            
            # if water, then return 0
            if grid[r][c] == 0:
                return 0
            
            # if already visited
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))
            
            # we have an area of at least 1, the current cell
            ar = [1]
            for d in directions:
                ar.append(dfs(r + d[0], c + d[1]))    
            
            # sum the areas from all directions
            res.append(sum(ar))
            return sum(ar)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    visisted = set()
                    dfs(r, c)
                
        return max(res)
        
            
        
        
        