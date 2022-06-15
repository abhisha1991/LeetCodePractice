# https://leetcode.com/problems/swim-in-rising-water/
from heapq import *
class Solution:
    # time complexity is n^2 log n
    # n^2 since we go through the grid which is n x n
    # log n since we push/pop at every cell

    # we need to minimize the maximum height that takes us to the target point
    # ie, the max height along this "minimum height path" is going to be our answer
    # https://www.youtube.com/watch?v=amvrKlMLuGY
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        # we're currently at 0,0
        visited.add((0,0))
        # the heap guarantees that we take the "minimum height path" explained above
        pq = []
        heapq.heapify(pq)
        # heap has elements as tuple (max height in this path, row, col)
        heapq.heappush(pq, (grid[0][0], 0, 0))
        
        rows = len(grid)
        cols = len(grid[0])
        
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        
        # res is going to be the min of the "max height of all possible paths" that reach the target 
        res = sys.maxsize
        
        while pq:
            h, r, c = heapq.heappop(pq)
            # print(f"reached point {r},{c} with max path height {h}")
            
            # if we've reached the dest point, recalculate res
            if r == rows-1 and c == cols-1:
                res = min(res, h)
            
            for d in directions:
                newr = r + d[0]
                newc = c + d[1]
                
                if newr >=0 and newc >=0 and newr < rows and newc < cols \
                and (newr, newc) not in visited:
                    # go in all directions from current r,c and push into the heap
                    
                    # because its a min heap, the row/col corresponding to the least max height path
                    # will be the one that bubbles on top of the heap and we'll take that path next 
                    
                    maxh = max(grid[newr][newc], h)
                    heapq.heappush(pq, (maxh, newr, newc))
                    visited.add((newr, newc))
        
        return res