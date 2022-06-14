# https://leetcode.com/problems/shortest-distance-from-all-buildings/
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        houses = collections.deque()
        lots = dict()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    houses.append((r,c))
                
                if grid[r][c] == 0:
                    # for the values
                    # first number is unique number of houses this empty lot can reach
                    # second number is total shortest dist from bfs that it takes to reach this r,c from all houses
                    lots[(r,c)] = [0, 0] 
                
        if len(lots) == 0:
            return -1
        
        hCount = len(houses)
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        # we're going to do a BFS from all houses to all empty plots of land
        # we're going to track 2 things, whether or not a given plot of land can be reached from house 'h'
        # and what is the dist from this house 'h' to the empty plot of land under consideration
        while houses:
            hr, hc = houses.popleft()
            # there is another optimization that can be done here
            # instead of re-initing the visited set over and over again, we can take our first
            # set of visited empty lots (that we know can reach the first house), 
            # and then use those to reach our other houses.
            # why? for a lot point to be valid, it must be reachable to all buildings
            # so if its not part of the first visited group, then its not reachable by at least 1 house
            visited = set()
            q = collections.deque()
            
            # populate the q initially
            # q contains unvisited empty plots of land
            for d in directions:
                newr = hr + d[0]
                newc = hc + d[1]
                
                if newr >= 0 and newc >= 0 and newr < rows and newc < cols \
                and grid[newr][newc] == 0 and (newr, newc) not in visited:
                    
                    visited.add((newr, newc)) 
                    q.append((newr, newc, 1))
            
            # do bfs on empty plots of land
            while q:
                r, c, dist = q.popleft()
                
                # distance from this house (hr, hc) is increased by 'dist'
                lots[(r, c)][1] += dist
                
                # this point is reachable by one more unique house (hr, hc)
                lots[(r, c)][0] +=1
                    
                for d in directions:
                    newr = r + d[0]
                    newc = c + d[1]
                    
                    if newr >= 0 and newc >= 0 and newr < rows and newc < cols \
                    and grid[newr][newc] == 0 and (newr, newc) not in visited:

                        visited.add((newr, newc))
                        q.append((newr, newc, dist+1))
                        
        mnDist = sys.maxsize
        for k,v in lots.items():
            # if current lot of land can reach all houses
            if v[0] == hCount:
                # take min dist
                mnDist = min(mnDist, v[1])
        
        return -1 if mnDist == sys.maxsize else mnDist