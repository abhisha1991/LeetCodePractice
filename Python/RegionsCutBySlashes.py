# https://leetcode.com/problems/regions-cut-by-slashes/
class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        # keep in mind -- g = [[0 for x in range(cols * 3)]] * (rows * 3) is NOT the same as below
        # why? https://stackoverflow.com/questions/6007881/what-does-the-0x-syntax-do-in-python
        g = [[0 for x in range(cols * 3)] for y in range(rows * 3)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '/':
                    # to visualie, try to imagine (1,1) was '/', then you'd have
                    # (5,3), (4,4) and (3,5) as '/' in the magnified array
                    # we are representing '/'' by 1
                    g[i * 3][(j * 3) + 2] = 1
                    g[(i * 3) + 1][(j * 3) + 1] = 1
                    g[(i * 3) + 2][j * 3] = 1
                elif grid[i][j] == '\\':
                    print("backward slash found at " + str(i) + " " + str(j))
                    # to visualie, try to imagine (1,1) was '\'
                    # then (3,3), (4,4), (5,5) would be '\'
                    # we are representing '\ by 1'
                    g[i * 3][j * 3] = 1
                    g[(i * 3) + 1][(j * 3) + 1] = 1
                    g[(i * 3) + 2][(j * 3) + 2] = 1
        
        countregions = 0
        print("g is ")
        print(g)
        for i in range(rows * 3):
            for j in range(cols * 3):
                # if the cell has not been explored - ie, its 0, 
                # explore all its neighbors using dfs
                # explore the neighbors by marking them with a special char, say '*'
                # once all cells have been explored, the region has been explored
                # so we have found 1 new region, so increment the region counter
                if g[i][j] == 0:
                    # this dfs explores a region and indentifies a new region
                    self.dfs(g, i, j)
                    countregions +=1
        
        return countregions
        
    def dfs(self, g, i, j):
        r = len(g)
        c = len(g[0])
        # if it is out of bounds or the array element has already been explored (rep by *) or it is a slash symbol (rep by 1)
        if i >= r or i < 0 or j >= c or j < 0  or g[i][j] == 1 or g[i][j] == '*':
            return
        g[i][j]= '*'
        self.dfs(g, i+1, j)
        self.dfs(g, i, j+1)
        self.dfs(g, i-1, j)
        self.dfs(g, i, j-1)
        