# https://leetcode.com/problems/dungeon-game/
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        rows = len(dungeon)
        cols = len(dungeon[0])
        grid = dungeon
        
        self.dp = []
        for i in range(rows):
            self.dp.append([sys.maxsize] * cols)
        
        def getHealth(cur, nxtR, nxtC):
            if nxtR < 0 or nxtC < 0 or nxtR >= rows or nxtC >= cols:
                return sys.maxsize
            
            # either right or bottom of current cell
            # this will always be a positive value, as seen when populating dp cells in func()
            nxt = self.dp[nxtR][nxtC]
            
            # we need at least one point to survive, thus the max
            '''
            why are we doing nxt-cur?
            nxt is always positive
            cur can be positive or negative
            
            if cur is negative, we know we want to return nxt + abs(cur) or nxt - cur
            ie, we will need extra 'cur' units of health to reach that cur cell to combat its -ve impact
            
            if cur is positive:
                if cur is larger than nxt (ie, large positive number > nxt), then, nxt-cur is -ve, 
                so we return max(1, -ve) = 1
                
                if cur is smaller than nxt, then to reach cur, we need nxt-cur units only
                example: say 2 is cur below and Q is the destination of the queen, x are other cells up/left
                      
                      x x  x
                      x 2  10
                      x 5  Q
                        
                then to reach cell '2' we will just need 3 units
            '''
            return max(1, nxt - cur)
        
        def func():
            # notice that we're going from bottom right to top left here
            for c in range(cols-1, -1, -1):
                for r in range(rows-1, -1, -1):
                    cur = grid[r][c]
                    
                    # try and get min health from the 
                    # right and bottom as those are the only 2 directions allowed
                    cur2right = getHealth(cur, r, c+1)
                    cur2down = getHealth(cur, r+1, c)
                    h = min(cur2right, cur2down)
                    
                    if h != sys.maxsize:
                        # we get back valid health
                        self.dp[r][c] = h
                    else:
                        if cur >= 0:
                            # if the current cell was >= 0
                            # then we must have 1 unit of health to reach this current cell
                            self.dp[r][c] = 1
                        else:
                            # if current cell is negative, 
                            # then we must have 1 + abs(cur) as min health to fight off the effect of -ve cur 
                            self.dp[r][c] = 1 + abs(cur)
                    
        
        func()
        return self.dp[0][0]