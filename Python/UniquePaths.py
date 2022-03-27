# https://leetcode.com/problems/unique-paths/description/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = []
        if m == 1 and n == 1:
            return 1
        
        for i in range(m):
            paths.append([0] * n)
            
        # paths[r][c] is going to be number of ways to get to m-1,n-1 from r,c
        # this will be total num of ways to reach m-1,n-1 from r+1,c and r,c+1
        def helper(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return 0
            
            if paths[r][c] != 0:
                return paths[r][c]
            
            if r == m-1 and c == n-1:
                return 1
            
            paths[r][c] = helper(r+1,c) + helper(r,c+1)
            return paths[r][c]
        
        helper(0, 0)
        # return total num of ways to reach r,c from the start, ie, 0,0
        return paths[0][0]