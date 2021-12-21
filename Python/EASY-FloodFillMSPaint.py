# https://www.geeksforgeeks.org/flood-fill-algorithm-implement-fill-paint/
class Solution(object):
    def floodfill(self, matrix, x, y, newC):
        oldC = matrix[x][y]
        self.helper(matrix, x, y, oldC, newC)
        return matrix

    def helper(self, matrix, x, y, oldC, newC):

        # if x or y are out of bounds of the array
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            return

        # if the current cell is not the old color, we cant replace it
        if matrix[x][y] != oldC:
            return

        # replace current pixel with new color
        matrix[x][y] = newC
        # replace adjacent pixels with new color if valid replacement
        self.helper(matrix, x + 1, y, oldC, newC)
        self.helper(matrix, x - 1, y, oldC, newC)
        self.helper(matrix, x, y + 1, oldC, newC)
        self.helper(matrix, x, y - 1, oldC, newC)