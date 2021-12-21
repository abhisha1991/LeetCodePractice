# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        maxrows = []
        maxcols = []
        res = 0
        for i in range(m):
            maxrow = 0
            for j in range(n):
                if grid[i][j] > maxrow:
                    maxrow = grid[i][j]
            maxrows.append(maxrow)
        
        for j in range(n):
            maxcol = 0
            for i in range(m):
                if grid[i][j] > maxcol:
                    maxcol = grid[i][j]         
            maxcols.append(maxcol)
        
        print(maxrows)
        print(maxcols)
        for i in range(m):
            for j in range(n):
                minrc = min(maxrows[i], maxcols[j])
                res += minrc - grid[i][j]
        return res
        