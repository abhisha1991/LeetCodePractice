# https://leetcode.com/problems/shortest-path-to-get-food
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        start = None
        food = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '*':
                    start = (i,j)
                
                if grid[i][j] == '#':
                    food.add((i,j))
        
        
        q = [(start[0], start[1], 0)]
        visited = set()
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        while q:
            r, c, dist = q.pop(0)
            
            if (r,c) in food:
                return dist
            
            for d in directions:
                newr = r + d[0]
                newc = c + d[1]
                
                if newr >= 0 and newc >=0 and newr < rows and newc < cols \
                and (newr, newc) not in visited and grid[newr][newc] != 'X':
                    visited.add((newr, newc))
                    q.append((newr, newc, dist+1))
        
        return -1