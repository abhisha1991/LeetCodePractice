# https://leetcode.com/problems/number-of-distinct-islands/
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        if rows == 0 or cols == 0:
            return 0
        
        islands = []
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        
        globalVisited = set()
        island = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            if (r,c) in island:
                return 
            
            if grid[r][c] == 0:
                return
            
            island.add((r,c))
            globalVisited.add((r,c))
            for d in dirs:
                dfs(r + d[0], c + d[1])
            
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in globalVisited:
                    island = set()
                    dfs(r,c)
                    islands.append(list(island))
        
        
        for i in range(len(islands)):
            a = list(sorted(islands[i]))
            # this is a clever idea -- we need to translate everything to the origin
            # by subtracting the first element from each element of the island co-ordinates
            # that way, if we had 2 islands
            # say one was [(2,3), (2,4)] and the other was say [(4,5), (4,6)]
            # then if we subtract first element, we get [(0,0), (0,1)] for both
            # so they're the same islands, just translated in different places
            islands[i] = [(a[x][0] - a[0][0], a[x][1] - a[0][1]) for x in range(len(a))]
        
        res = []
        for i in islands:
            if i not in res:
                res.append(i)
                
        return len(res)