# https://leetcode.com/problems/n-queens
# https://www.youtube.com/watch?v=Ph95IHmRp5M
class Solution:
    def generateEmptyChess(self, n):
        chess = []
        for i in range(n):
            chess.append(["."] * n)
        return chess
    
    def solveNQueens(self, n: int) -> List[List[str]]:            
        res = []
        chess = self.generateEmptyChess(n)
        # if we have a queen in a col, we cannot place another queen in the same col. 
        # this set ensures that it doesn't happen
        col = set()
        
        # if we have a queen in the positive diagonal, then we cant place another queen along that diag
        # example -- consider n=4 and points (0,3), (1,2), (2,1), (3,0) -- these are points on the positive diag
        # their r+c is constant, ie, 3
        posDiag = set()
        
        # if we have a queen in the negative diagonal, then we cant place another queen along that diag
        # example -- consider n=4 and points (0,1), (1,2), (2,3) -- these are points on the negative diag
        # their r-c is constant, ie, -1
        negDiag = set()
        
        def queens(r):
            if r == n:
                placement = ["".join(row) for row in chess]
                res.append(placement)
                return
            
            for c in range(n):
                # this means that the col where we're trying to place a queen is already in the "attack vector" of another 
                # already placed queen
                if c in col or r+c in posDiag or r-c in negDiag:
                    continue
                
                # found a valid place to have the queen
                # reserve that spot, so no other queen can be placed there
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                # place a queen there
                chess[r][c] = 'Q'
                
                queens(r+1)
                
                # unreserve that spot
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                # remove a queen from there
                chess[r][c] = '.'
                
        # since there have to be n queens placed, there has to be 1 queen per row
        # this means there has to be a queen on the top row
        # start with the 1st row, ie, then go through every col position placing 1 queen at a time within that row
        queens(0)
        return res