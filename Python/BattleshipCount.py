# https://leetcode.com/problems/battleships-in-a-board/
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if len(board) == 0: return 0
        count = 0 # total number of battleships
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    flag = 1 # potential battleship found
                    if i > 0 and board[i-1][j] == 'X': flag = 0 # we've previously counted for previous i
                    if j > 0 and board[i][j-1] == 'X': flag = 0 # we've previously counted for previous j
                        
                    count +=flag
                    
        return count