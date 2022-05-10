# https://leetcode.com/problems/shortest-path-in-binary-matrix
class Solution:
    def __init__(self):
        self.path = sys.maxsize
        
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [1,1], [-1,0], [0,-1], [-1,-1], [1,-1], [-1,1]]
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        q.append((0,0,1))
        
        while q:
            r, c, steps = q.popleft()
            if r < 0 or c < 0 or r >= rows or c >= cols:
                continue
            
            if (r,c) in visited:
                continue
            
            if grid[r][c] == 1:
                continue
            
            visited.add((r,c))
            
            for d in directions:
                q.append((r + d[0], c + d[1], steps+1))
            
            if r == rows-1 and c == cols-1:
                if steps < self.path:
                    self.path = steps
                    
        if self.path == sys.maxsize:
            return -1
        return self.path