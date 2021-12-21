# https://leetcode.com/problems/valid-sudoku/description/
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # validate each row
        for i in range(len(board)):
            dic = dict()
            for j in range(len(board)):
                if board[i][j] != '.':
                    # each row must have only a given number once in occurrence in dic
                    if board[i][j] in dic.keys():
                        return False
                    dic[board[i][j]] = 1

        # validate each column
        # THE ZIP FUNCTION AND ITS ROLE, VERY IMPORTANT CONCEPT
        # https://stackoverflow.com/questions/13704860/zip-lists-in-python
        for i in zip(*board):
            dic = dict()
            col = list(i)
            for k in col:
                # each col must have only a given number once in occurrence in dic
                if k != '.' and k in dic.keys():
                    return False
                dic[k] = 1

        # validate each square
        # VERY VERY IMPORTANT HERE, LOOK AT THE ITERATION OF i,j - THE ITERABLE IS A SET, NOT A RANGE
        # HENCE, i WILL TAKE ON VALUES, 0, 3, 6, (ALL VALUES OF THE SET)
        #  - WHICH IS THE BEGINNING ROWS OF EACH SUB SQUARE
        # j WILL TAKE ON VALUES 0, 3, 6 - WHICH ARE THE BEGINNING VALUES OF EACH OF THE COLUMNS OF THE SQUARES
        '''
        in this soduku, 0 is the spot for each i,j pair from the below iteration
        0 X X 0 X X 0 X X
        X X X X X X X X X
        X X X X X X X X X
        0 X X 0 X X 0 X X
        X X X X X X X X X
        X X X X X X X X X
        0 X X 0 X X 0 X X
        X X X X X X X X X
        X X X X X X X X X
        '''
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                dic = dict()
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                # each square must have only a given number once in occurrence in dic
                for k in square:
                    if k != '.' and k in dic.keys():
                        return False
                    dic[k] = 1
        return True