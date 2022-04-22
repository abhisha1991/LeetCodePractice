# https://leetcode.com/problems/walls-and-gates/
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # define constants
        # inf indicates empty room
        empty = 2147483647
        gate = 0
        wall = -1
        
        visited = set()
        rows = len(rooms)
        cols = len(rooms[0])
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        
        # dfs gets TLE for some reason
        def dfs(r, c, dist):
            if r < 0 or c < 0 or r >= rows or c >= cols: 
                return
            
            if (r,c) in visited:
                return
            
            visited.add((r,c))
            
            if rooms[r][c] == wall:
                return
            
            if dist < rooms[r][c]:
                rooms[r][c] = dist
            
            for d in dirs:
                dfs(r + d[0], c + d[1], dist+1)
            
            visited.remove((r,c))
        
        # q for bfs
        q = []
        for i in range(rows):
            for j in range(cols):
                # this is the key insight, instead of starting at every empty room and working
                # toward reaching a gate, start a dfs/bfs at the gate and reach every empty room
                if rooms[i][j] == gate:
                    q.append((i, j))
                    # dfs(i, j, 0)
        

        # do bfs
        while q:
            item = q.pop(0)
            r = item[0]
            c = item[1]
            dist = rooms[r][c]
            
            for d in dirs:
                newr = r + d[0]
                newc = c + d[1]
                
                if newr < 0 or newc < 0 or newr >= rows or newc >= cols:
                    continue
                
                # we have already considered gates in q 
                # we don't want to do anything on walls either
                # so the condition is that if the cell is anything but an empty room, we discard
                if rooms[newr][newc] != empty:
                    continue
                
                rooms[newr][newc] = min(dist + 1, rooms[newr][newc])
                q.append((newr, newc))