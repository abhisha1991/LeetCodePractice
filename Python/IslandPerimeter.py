# https://leetcode.com/problems/island-perimeter
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.perimeter = 0
        
        visited = set()
        
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            if (r,c) in visited:
                return
            
            if grid[r][c] == 0:
                return
            
            visited.add((r,c))
            
            # process the cell (r,c)
            for d in directions:
                newr = r + d[0]
                newc = c + d[1]
                
                # if cell is at the edge of grid, then we are surrounded by water around
                # so we need to increase perimeter
                if newr < 0 or newc < 0 or newr >= rows or newc >= cols:
                    self.perimeter +=1
                    continue
                
                # if cell's neighbor is water, we also need to increase perimeter
                if grid[newr][newc] == 0:
                    self.perimeter +=1
            
            
            for d in directions:
                dfs(r + d[0], c + d[1])
        
        
        for r in range(rows):
            for c in range(cols):
                # find the first cell that is land and enter into dfs only once to explore full island
                if grid[r][c] == 1:
                    dfs(r,c)
                    break
                
        return self.perimeter