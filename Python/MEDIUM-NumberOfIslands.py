# https://leetcode.com/problems/number-of-islands/description/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        count = 0
        for r in range(rows):
            for c in range(cols):
                grid[r][c] = int(grid[r][c])
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            if (r,c) in visit or grid[r][c] == 0:
                return
            
            visit.add((r, c))
                
            for d in directions:
                dfs(r + d[0], c + d[1])
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    
                    v = len(visit)
                    dfs(r, c)

                    # only when the visit set increases in members
                    # should we add the number of islands
                    if len(visit) > v:
                        count +=1
        
        return count
