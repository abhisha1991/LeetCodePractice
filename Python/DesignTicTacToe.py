# https://leetcode.com/problems/design-tic-tac-toe/
# this is an o(n) solution, which works but is not optimal
# there is an o(1) solution 
class TicTacToe:

    def __init__(self, n: int):
        self.matrix = []
        self.n = n
        for i in range(n):
            arr = ['#'] * n
            self.matrix.append(arr)
        
        
    def move(self, row: int, col: int, player: int) -> int:
        self.matrix[row][col] = player
        
        # check row
        flag = True
        
        for i in range(self.n):
            if self.matrix[i][col] != player:
                flag = False
                break
        
        if flag:
            return player
        
        # check col        
        flag = True
        
        for i in range(self.n):
            if self.matrix[row][i] != player:
                flag = False
                break
        
        if flag:
            return player
        
        # check diagonal
        flag = True
        
        for i in range(self.n):
            if self.matrix[i][i] != player:
                flag = False
                break
        
        if flag:
            return player
        
        # check anti diagonal
        flag = True
        
        for i in range(self.n):
            if self.matrix[i][self.n-1-i] != player:
                flag = False
                break
        
        return player if flag else 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)