# https://leetcode.com/problems/unique-paths/description/
# concept is simple - use recursion, store the results in a mat so you dont have to re-calculate the results everytime
class Solution:
    def __init__(self):
        self.mat = []

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = self.commonRetVals(m, n)
        if res is not None:
            return res

        for i in range(0, m):
            self.mat.append([-1] * n)

        self.mat[0][0] = 0
        if m > 0 and n > 0:
            self.mat[1][0] = 1
            self.mat[0][1] = 1

        self.helper(m - 1, n - 1)
        print(self.mat)
        '''
        m = rows
        n = columns
        6 3 1
        3 2 1 <-- this index is mat[1][0]
        1 1 0
        Here we have an inverted matrix in which we store our results
        matrix is [[0, 1, 1], [1, 2, 3], [1, 3, 6]]
        which is basically inverted, hence we return index -> m-1, n-1 (top left)
        right bottom is 0,0
        rows and columns move from bottom to up, right to left
        '''
        return self.mat[m - 1][n - 1]

    def helper(self, m, n):
        # cant have invalid indices
        if m < 0 or n < 0:
            return 0

        print("current m is", m)
        print("current n is", n)
        if self.mat[m][n] is not -1:
            return self.mat[m][n]

        # ways to reach from m,n to 0,0 is to sum ways going down + going right
        self.mat[m][n] = self.helper(m - 1, n) + self.helper(m, n - 1)
        return self.mat[m][n]

    def commonRetVals(self, m, n):
        if m is 0 or n is 0:
            return 0
        # if there's only one row or 1 column, the only way to reach is either go all down or all right
        if m is 1 or n is 1:
            return 1
        return None