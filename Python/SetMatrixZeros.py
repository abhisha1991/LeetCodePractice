# https://leetcode.com/problems/set-matrix-zeroes/description/
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        while count < len(matrix):
            if count in rows:
                matrix[count] = [0] * len(matrix[0])
            count += 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j in cols:
                    matrix[i][j] = 0