# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
class Solution:
    # the algo is pretty simple
    # we're looking at a given cell, r,c -- for this we take a look at the max height in current row, max height in current col
    # these are the 2 heights which we can possibly increase by - hr, hc
    # we need the min of these so as to not disrput the skyline
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        # take transpose of the matrix to make it column major
        # so you can grab a column at once
        gridT = [[grid[j][i] for j in range(n)] for i in range(n)]
        
        for r in range(n):
            for c in range(n):
                h_minmax = min([max(grid[r]), max(gridT[c])])
                # remember we're adding the differnce between our curr height and the max allowed from above
                res += h_minmax - grid[r][c]
                
        return res
        