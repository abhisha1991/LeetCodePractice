# https://leetcode.com/problems/the-maze/
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dr, dc = destination[0], destination[1]
        sr, sc = start[0], start[1]
        
        rows = len(maze)
        cols = len(maze[0])
        
        q = [start]
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        
        while q:
            i, j = q.pop(0)
            # mark as visited
            maze[i][j] = 2

            if i == dr and j == dc:
                return True
            
            for d in dirs:
                row = i + d[0]
                col = j + d[1]
                while 0 <= row < rows and 0 <= col < cols and maze[row][col] != 1:
                    row += d[0]
                    col += d[1]
                
                # we overstretched when coming out of loop, 
                # so retract one to keep the above condition of bounds to be true
                row -= d[0]
                col -= d[1]
                
                # add to queue only if unvisited
                if maze[row][col] == 0:
                    q.append([row, col])
        
        return False