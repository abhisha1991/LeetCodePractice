# implementation is correct, but needs memoization, gets TLE on Leetcode
# https://leetcode.com/problems/knight-dialer/
class Solution:
    def __init__(self):
        self.paths = set()
        
    def knightDialer(self, n: int) -> int:
        grid = []
        # create phone key pad
        # with -1 indicating no jump zone
        grid.append([1, 2, 3])
        grid.append([4, 5, 6])
        grid.append([7, 8, 9])
        grid.append([-1, 0, -1])
        mod = 10**9 + 7
        rows = len(grid)
        cols = len(grid[0])
        
        dirs = [[-2,1], [-2,-1], [-1,2], [1,2], [2,1], [2,-1], [-1,-2], [1,-2]]
        
        def dfs (r, c, remain, path):
            if remain == 0:
                self.paths.add(path)
                return
            
            if r >= rows or c >= cols or r < 0 or c < 0:
                return
            
            if grid[r][c] == -1:
                return
            
            for d in dirs:
                dfs(r + d[0], c + d[1], remain-1, path + str(grid[r][c]))
            
        
        for i in range(rows):
            for j in range(cols):
                # not allowed to be in the no jump zone
                if (i == 3 and j == 0) or (i == 3 and j == 2):
                    continue
                dfs(i, j, n, '')
        
        # print(sorted(list(self.paths)))
        return len(self.paths) % mod