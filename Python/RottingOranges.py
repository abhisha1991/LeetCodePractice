# https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        rows = len(grid)
        cols = len(grid[0])
        
        isFreshOrange = False
        
        for i in range(rows):
            for j in range(cols):
                # collect all rotten oranges in queue
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                
                # check if there's at least 1 fresh orange
                # used for edge cases below
                elif grid[i][j] == 1:
                    isFreshOrange = True
        
        # no rotten oranges but fresh exists, so its impossible to infect fresh orange
        if not q and isFreshOrange:
            return -1
        
        # no rotten oranges, but fresh one doesn't exist, so time to rot is 0, not -1
        if not q and not isFreshOrange:
            return 0
        
        visited = set()
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        # time to rot
        # captures the min time taken to rot for all oranges in the grid
        ttr = -sys.maxsize
        
        while q:
            rotten = q.pop(0)
            r = rotten[0]
            c = rotten[1]
            ts = rotten[2]
            
            visited.add((r,c))
            for d in dirs:
                newr = r + d[0]
                newc = c + d[1]
                
                # out of bounds
                if newr < 0 or newc < 0 or newr >= rows or newc >= cols:
                    continue
                
                # already visited, avoid infinite q
                if (newr, newc) in visited:
                    continue
                
                # if it is empty space, ignore, if already rotten - it should have been added to q
                # either in the "initial q population" phase or in the "infect" phase
                if grid[newr][newc] != 1:
                    continue
                
                # make existing orange rot and increment time by 1
                grid[newr][newc] = 2
                q.append((newr, newc, ts+1))
                
                # time to rot is going to be the max time of infection in bfs seen so far
                # or ttr itself
                ttr = max(ttr, ts+1)
        
        # if there is still a fresh orange present, then it is impossible to make it rotten
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        # ttr was init to -sys.maxsize so return max of 0 and valid ttr
        return max(0, ttr)