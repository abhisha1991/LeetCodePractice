# https://leetcode.com/problems/making-a-large-island/
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        
        # dictionary containing idx = key, and val = list.
        # idx is just a "group number" for the area of the points belonging to the group
        # for example, grid = [[0,1,0],[0,1,0],[0,0,1]] will have 2 area groups 
        # area[0] = [set((0,1),(1,1)), 2]
        # area[1] = [set((2,2)), 1]
        
        # list contains 2 elements, 1st element is a set of co-ordinates that make up that area
        # 2nd element of list is the actual area value
        area = dict()
        # this is the group number, ie, the key of the dictionary above
        areaCounter = 0
        
        def findAreas(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            if grid[r][c] == 0:
                return
            
            if (r,c) in visit:
                return
            
            # grid[r][c] is 1, so add this point to the visited set
            visit.add((r,c))
            
            for d in directions:
                findAreas(r + d[0], c + d[1])
            
            added = False
            for k,v in area.items():
                # if there is a subset of our set
                # or if there is a set equal to our set
                # replace with our newly found area
                if v[0].issubset(set(visit)):
                    area[k] = [set(visit), len(set(visit))]
                    added = True
                    break
                
                # if we are already a subset in the dictionary
                # then our area is already covered by another dfs run
                if set(visit).issubset(v[0]):
                    added = True
                    break
                
            if not added:
                area[areaCounter] = [set(visit), len(set(visit))]
                
            return
        
        # get area groups without toggle
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    visit = set()
                    findAreas(r,c)
                    
                areaCounter +=1
        
        # now go through all zero area values and try and toggle them to 1
        # note that at most one means either don't toggle or toggle once
        # we have the areas as a result of 'not toggling' from before
        # now its time to toggle
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    grid[r][c] = 1
                    visit = set()
                    findAreas(r,c)
                    # replace back to 0
                    grid[r][c] = 0
                    
                areaCounter +=1
                
        
        # return max area after toggle
        maxArea = 0
        for k,v in area.items():
            if maxArea < v[1]:
                maxArea = v[1]
        return maxArea