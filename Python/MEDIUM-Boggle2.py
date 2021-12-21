from copy import deepcopy


class Solution:
    def __init__(self):
        self.boardcopy = []

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                # no need to find potential positions, just start sequentially, else you'll be forced to do a O(n2)
                if self.helper(board, word[0], word[1:], i, j):
                    return True

        return False

    def helper(self, board, w, rest, i, j):
        # print("exploring for nbor", i, j)
        # print("current board", board)
        # if the index is invalid, its false, no need to find nbors!
        # if the first char is not equal to the the board char, return false
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or w != board[i][j]:
            return False

        if len(rest) is 0 and w == board[i][j]:
            return True
        # save board char in temp, in case things dont work out and you've to reset the value of i,j
        temp = board[i][j]
        # assign i,j to a special value which implies position is visited, no need to maintain a visited array
        board[i][j] = '#'

        first = rest[0]
        rest = rest[1:]
        # check if there are any successes from any nbors
        exist = self.helper(board, first, rest, i - 1, j) or self.helper(board, first, rest, i + 1, j) or self.helper(
            board, first, rest, i, j - 1) or self.helper(board, first, rest, i, j + 1)
        # if not, reset the board value to the earlier saved value
        if not exist:
            board[i][j] = temp
            return False
        return True