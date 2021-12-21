class Solution:
    def __init__(self):
        self.res = []

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        '''
        [-4, -5, -6, 0, 0],
        [-1, -2, -3, 0, 0],
        [ 1, 2, 3,   0, 0],
        [ 4, 5, 6,   0, 0],
        [ 7, 8, 9,   0, 0]
        top, bottom, left, right
        x = left -> right [top][x] -- AT THE END, top++ 
        x = top -> bottom [x][right] -- AT THE END, right--
        x = right -> left [bottom][x] -- AT THE END, bottom--
        x = bottom -> top [x][left] -- AT THE END, left++
        '''
        if matrix == []:
            return []
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m -1
        left = 0
        right = n - 1
        if bottom is 0:
            return matrix[0]

        while top <= bottom and left <= right:
            if self.checkLen(m, n): break
            x = left
            while x <= right:
                self.res.append(matrix[top][x])
                x += 1
            top += 1
            x = top
            if self.checkLen(m, n): break
            while x <= bottom:
                self.res.append(matrix[x][right])
                x += 1
            right -= 1
            x = right
            if self.checkLen(m, n): break
            while x >= left:
                self.res.append(matrix[bottom][x])
                x -= 1
            bottom -= 1
            x = bottom
            if self.checkLen(m, n): break
            while x >= top:
                self.res.append(matrix[x][left])
                x -= 1
            left += 1
        print(self.res)
        return self.res

    def checkLen(self, m, n):
        if len(self.res) == m * n:
            return True
        return False

s = Solution()
s.spiralOrder([[6], [7], [9]])