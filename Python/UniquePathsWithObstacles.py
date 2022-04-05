# https://leetcode.com/problems/unique-paths-ii/
# see this for inspiration: https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        grid = obstacleGrid
        
        # convert to non numeric because we want to store results in place
        # and 1 or 0 would mean there are 1 or 0 paths from that cell (r,c) to the destination
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = '#'
                else:
                    grid[i][j] = None
        
        # if the destination is blocked, we cant do much
        # if the source is blocked, we cant do much
        if grid[rows-1][cols-1] == '#' or grid[0][0] == '#':
            return 0
        
        if rows - 1 == 0 and cols - 1 == 0:
            # we have something like [[0]]
            return 1
        
        visit = set()
        directions = [[0,1],[1,0]]
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            
            if (r,c) in visit:
                return 0
            
            if r == rows - 1 and c == cols - 1:
                return 1
            
            if grid[r][c] == '#':
                return 0
            
            # if that cell has already been calculated
            # return stored result (memoization)
            if grid[r][c] != None:
                return grid[r][c]
            
            visit.add((r,c))
            # set to 0, because it is currently None
            grid[r][c] = 0
            for d in directions:
                grid[r][c]  += dfs(r + d[0], c + d[1])
            
            visit.remove((r,c))
            return grid[r][c]
        
        dfs(0, 0)
        
        return grid[0][0]