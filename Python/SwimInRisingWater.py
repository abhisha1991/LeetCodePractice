# https://leetcode.com/problems/swim-in-rising-water/
from heapq import *
class Solution:
    # time complexity is n^2 log n
    # n^2 since we go through the grid which is n x n
    # log n since we push/pop at every cell
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        # we're currently at 0,0
        visited.add((0,0))
        pq = []
        heapq.heapify(pq)
        # heap has elements as tuple (grid val, row, col)
        heapq.heappush(pq, (grid[0][0], 0, 0))
        
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        
        while pq:
            h, r, c = heapq.heappop(pq)
            # print(f"reached point {r},{c} with height {h}")
            
            # res is going to be the max height we have seen so far in our path
            res = max(res, h)
            
            # if we've reached the dest point, return res
            if r == rows-1 and c == cols-1:
                return res
            
            for d in directions:
                newr = r + d[0]
                newc = c + d[1]
                
                if newr >=0 and newc >=0 and newr < rows and newc < cols \
                and (newr, newc) not in visited:
                    # go in all directions from current r,c and push into the heap
                    
                    # because its a min heap, the row/col corresponding to the least grid[newr][newc]
                    # will be the one that bubbles on top of the heap and we'll take that path next 
                    heapq.heappush(pq, (grid[newr][newc], newr, newc))
                    visited.add((newr, newc))