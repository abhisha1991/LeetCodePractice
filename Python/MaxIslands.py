# https://leetcode.com/problems/max-area-of-island
class Solution(object):
    def __init__(self):
        self.count = 0
        self.m = 0
        self.n = 0
        self.counts = []
        
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.m = len(grid)
        self.n = len(grid[0])
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.count = 0
                    self.dfs(i, j, grid)
                    self.counts.append(self.count)
                else:
                    self.count = 0
                    
        if not self.counts:
            return 0
        
        return max(self.counts)
    
    def isvalid(self, i, j):
        if i < 0 or i >= self.m or j < 0 or j >= self.n:
            return False
        return True
        
    def dfs(self, i, j, grid):
        if self.isvalid(i , j) == False:
            return False
        
        if grid[i][j] == 0 or grid[i][j] == '#':
            return False
        
        # mark i,j as visited
        grid[i][j] = '#'
        self.count +=1
        
        self.dfs(i+1, j, grid)
        self.dfs(i, j+1, grid)
        self.dfs(i-1, j, grid)
        self.dfs(i, j-1, grid)
        
        return True
        
            
        
        
        