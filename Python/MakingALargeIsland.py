# https://leetcode.com/problems/making-a-large-island/
# https://www.youtube.com/watch?v=rmxZp7tlT0g
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        # dictionary containing key = group, and val = max area.
        area = dict()
        # this number idx=2 is important
        # the grid consists of 0,1 so we have to start with 2
        # the 2 by itself doesn't mean anything numerically, its just an index representing a unique "group"
        # so all cells in the island belonging to group 2 will be changed to grid[r][c] = 2
        # all cells in the island belonging to group 3 will be changed to grid[r][c] = 3 and so on
        idx = 2
        def findArea(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            if (r,c) in visit:
                return 0
            
            # if the cell belongs to our group already
            # or if it has been captured as part of some other group's area
            # then we cant count it as part of of our area
            if grid[r][c] == idx or grid[r][c] != 1:
                return 0
            
            # mark that cell to be part of that group
            grid[r][c] = idx
            visit.add((r,c))
            
            for d in directions:
                findArea(r + d[0], c + d[1])
            
            if idx not in area:
                area[idx] = len(visit)
            else:
                if area[idx] < len(visit):
                    area[idx] = len(visit)
            
        hasZero = False
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    hasZero = True
                    continue
                    
                if grid[r][c] == 1:
                    # pass a fresh empty visit set every time we do dfs
                    visit = set()
                    findArea(r,c)
                    
                    idx +=1
        
        # if all elements in the grid are 1
        if not hasZero:
            return rows * cols
        
        # calculate the maxArea so far
        # this is the max area assuming that we didn't flip any 0 cell to a 1
        for k,v in area.items():
            if v > maxArea:
                maxArea = v
        
        def sumNborAreas(r, c):
            # this dictionary is going to hold the total area of the current cell being "1" + all its neighbor island areas
            # key is island group number, value is area of that island group
            # currently, we have an area of 1, which is just the current cell area given that we "flipped" the cell from 0 to 1
            nborArea = {0: 1}
            
            # you may ask, why don't we use a simple list to keep track of the ares above, instead of using a dictionary
            # this is because we may have a situation where a cell is surrounded on 2 or more sides, say east and north
            # by the SAME island group (say 3). In such a case, if we use a list, we will add area[3] twice to nborArea instead of once
            
            # move in all neighbor directions
            for d in directions:
                newr = r + d[0]
                newc = c + d[1]
                
                if newr < 0 or newc < 0 or newr >= rows or newc >= cols:
                    # invalid neighbor, rep group by -1 (say)
                    nborArea[-1] = 0
                else:
                    group = grid[newr][newc]
                    if group is not 0:
                        nborArea[group] = area[group]
            
            # return self area (1) + sum of all neighbor island areas
            return sum(nborArea.values())
        
        # now actually "flip" a 0 cell to a 1 and see if you can "union" multiple island groups and update maxArea
        # we don't actually update any 0 cell to 1 in the grid, we just update the area assuming we did
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    ar = sumNborAreas(r, c)
                    # set the maxArea assuming that we flipped the current (r,c) to 1 and connected adjacent islands
                    if ar > maxArea:
                        maxArea = ar
        
        return maxArea