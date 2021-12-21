# https://leetcode.com/problems/rotate-image/description/

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        '''
        Consider example
        [[1,2,3,4,5,6],
        [7,8,9,10,11,12], 
        [13,14,15,16,17,18], 
        [19,20,21,22,23,24],
        [25,26,27,28,29,30],
        [31,32,33,34,35,36]]
        
        Basic concept is to rotate element by element - there are 4 pointers - i, j, k, l
        i points to left to right on the top row
        j points to top to bottom on the right most column
        k points to right to left on the bottom row
        l points to bottom to top on the left most column
        '''
        if matrix is None:
            return None
        n = len(matrix)

        count = 1
        while count <= n / 2:
            i = count - 1
            j = count - 1
            k = n - 1 - (count - 1)
            l = n - 1 - (count - 1)
            while i <= n - 1 - count:
                temp = matrix[count - 1][i]  # store 1 in temp
                matrix[count - 1][i] = matrix[l][count - 1]  # store 31 in 1's place
                temp2 = matrix[j][n - 1 - (count - 1)]  # store 6 in temp2
                matrix[j][n - 1 - (count - 1)] = temp  # store 1 in 6's place
                temp3 = matrix[n - 1 - (count - 1)][k]  # store 36 in temp3
                matrix[n - 1 - (count - 1)][k] = temp2  # store 6 in 36's place
                matrix[l][count - 1] = temp3  # store 36 in 31's place

                i += 1
                j += 1
                k -= 1
                l -= 1

            count += 1