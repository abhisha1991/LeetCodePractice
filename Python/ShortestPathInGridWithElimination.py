# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        # prioritize going down and right first, over left and up,
        # because we're trying to go to the bottom right of the grid
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        
        # if we have sufficient quota to remove all walls, then just return with manhattan dist
        # ie, go all the way bottom and go all the way right
        if k >= rows + cols - 2:
            return rows + cols - 2
        
        q = deque()
        q.append((0, 0, k, 0))
        
        def inBounds(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False
            return True
        
        while q:
            r, c, curK, steps = q.popleft()
            visited.add((r,c))
            
            # bfs always returns the shortest dist, so we can return early
            # this is a very important point to understand
            # dfs is not guaranteed to find shortest path, but bfs is
            if r == rows-1 and c == cols-1:
                return steps
            
            if curK < 0:
                continue
            
            if curK == 0 and grid[r][c] == 1:
                continue
            
            if grid[r][c] == 1 and curK > 0:
                curK -=1
            
            for d in directions:
                newr = r + d[0] 
                newc = c + d[1]  
                if (newr, newc) not in visited and inBounds(newr, newc):
                    q.append((newr, newc, curK, steps+1))
        
        return -1