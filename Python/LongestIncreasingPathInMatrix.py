# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
class Solution(object):
    def __init__(self):
        self.dp = []

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        maxi = 0
        if len(matrix) == 0:
            return maxi

        if len(matrix[0]) == 0:
            return maxi

        self.dp = [[0] * len(matrix[0]) for x in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dp[i][j] = self.helper(matrix, i, j)
                if self.dp[i][j] > maxi:
                    maxi = self.dp[i][j]

        # you'll have to add 1 to maxi, as we didnt count ourselves in the path when finding the path from us
        return maxi + 1

    def helper(self, matrix, i, j):
        # if dp of current is more than 0, we've already solved the problem for this current
        if self.dp[i][j] > 0:
            return self.dp[i][j]

        nbors = self.getNbors(matrix, i, j)
        # if any of nbors are bigger than you, you know you have somewhere to go, so add 1 for your result
        if len(nbors) > 0:
            self.dp[i][j] += 1

        temp = 0
        for n in nbors:
            # temp = the max path length from your neighbors
            if temp < self.helper(matrix, n[0], n[1]):
                temp = self.dp[n[0]][n[1]]

        # add to your current path length
        self.dp[i][j] += temp

        # return your longest path
        return self.dp[i][j]

    def getNbors(self, matrix, x, y):
        nbors = []
        temp = []
        temp.append((x - 1, y))
        temp.append((x + 1, y))
        temp.append((x, y + 1))
        temp.append((x, y - 1))

        for i in temp:
            if i[0] >= 0 and i[1] >= 0 and i[0] <= len(matrix) - 1 and i[1] <= len(matrix[0]) - 1:
                # if the coordinates are valid and are greater than current value [contributing to increasing path]
                if matrix[i[0]][i[1]] > matrix[x][y]:
                    nbors.append(i)
        return nbors