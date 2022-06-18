# https://leetcode.com/problems/bomb-enemy/
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        enemyCount = []
        for r in range(rows):
            enemyCount.append([0] * cols)
            
        res = 0
        
        '''
        carry out the algo in 2 stages

        STAGE 1: do a top to bottom, left to right sweep
        in this sweep, we are trying to sum up 2 things:
            1. enemies to the left of a given cell (r,c) and 
            2. enemies on the top of a given cell (r,c)
        
        STAGE 2: do a bottom to top, right to left sweep
        in this sweep, we are trying to sum up 2 things:
            1. enemies to the right of a given cell (r,c)
            2. enemies on the bottom of a given cell (r,c)
        '''
        
        # STAGE 1
        
        # counts the number of enemies to the LEFT of current cell (r,c) in the SAME row
        # this resets to 0 every time we hit a wall
        rowCount = 0
        # counts the number of enemies in that col seen so far from TOP for a given cell (r,c)
        # resets to 0 every time we hit a wall
        colCount = [0] * cols
        
        for r in range(rows):
            # we initialize to 0 for every new row since its counting number of enemies to the left and we're at 0th col
            # but the colCount state carries forward
            rowCount = 0
            for c in range(cols):
                # when we encounter an enemy, then there is a row and col hit
                if grid[r][c] == 'E':
                    rowCount +=1
                    colCount[c] +=1
                
                elif grid[r][c] == 'W':
                    # reset row count when we hit a wall
                    rowCount = 0
                    # set col count for pos 'c' for the next row to be 0
                    # the resetting of col count is the more interesting case
                    '''
                    imagine a single column in the grid, lets walk through colCount variable when iterating through rows
                    
                    E --> colCount[c] = 0 (initially its 0, now it increments to 1 for the next row for this col 'c')
                    0 --> colCount[c] = 1 (from previous row's col count evaluation for this pos 'c')
                    E --> colCount[c] = 2 (now it is made 2 since we encountered another enemy here)
                    W --> colCount[c] = 0 (reset col count since we hit a wall)
                    0 --> colCount[c] = 0 (col count is 0 since we reset it above, even though there were 2 'E' in same col)
                    '''
                    colCount[c] = 0
                
                # calculate total hits from row and col since we hit an empty spot where we can place a bomb
                elif grid[r][c] == '0':
                    enemyCount[r][c] += rowCount + colCount[c]
                    res = max(res, enemyCount[r][c])
                
        # STAGE 2
        
        # reinit rowCount and colCount to 0
        # now rowCount/colCount has a different meaning
        
        # counts the number of enemies to the RIGHT of current cell (r,c) in the SAME row
        # this resets to 0 every time we hit a wall
        rowCount = 0
        # counts the number of enemies in that col seen so far from BOTTOM for a given cell (r,c)
        # resets to 0 every time we hit a wall
        colCount = [0] * cols
        
        for r in range(rows-1, -1, -1):
            rowCount = 0
            for c in range(cols-1, -1, -1):
                if grid[r][c] == 'E':
                    rowCount +=1
                    colCount[c] +=1
                
                elif grid[r][c] == 'W':
                    rowCount = 0
                    colCount[c] = 0
                
                elif grid[r][c] == '0':
                    enemyCount[r][c] += rowCount + colCount[c]
                    res = max(res, enemyCount[r][c])
        
        return res

    # TLE since the time complexity is O(W * H * (W+H))
    # for every location, you check if there is an empty space
    # for that empty space, you look in the row and col to determine whether there are enemies or not (W+H)
    def maxKilledEnemies2(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        # find all bomb locations
        bomb = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0':
                    bomb.append((i,j))
        
        q = bomb
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        ans = 0
        while q:
            r,c = q.pop(0)
            
            count = 0
            # check in forward direction
            rr = r
            cc = c
            while rr < rows:
                if grid[rr][c] == 'W':
                    break
                if grid[rr][c] == 'E':
                    count +=1
                rr +=1
            
            while cc < cols:
                if grid[r][cc] == 'W':
                    break
                if grid[r][cc] == 'E':
                    count +=1
                cc +=1
            
            # check in backward direction
            rr = r
            cc = c
            while rr >= 0:
                if grid[rr][c] == 'W':
                    break
                if grid[rr][c] == 'E':
                    count +=1
                rr -=1
            
            while cc >= 0:
                if grid[r][cc] == 'W':
                    break
                if grid[r][cc] == 'E':
                    count +=1
                cc -=1
            
            ans = max(ans, count)
        
        return ans