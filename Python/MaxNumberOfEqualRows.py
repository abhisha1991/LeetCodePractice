# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        # solve2 is more time efficient
        return self.solve2(matrix)
        
    def solve1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ans = 0
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            flip = [0] * cols
            # flip will store the opposite of the current row
            for j in range(cols):
                flip[j] = 1 - matrix[i][j]
            count = 0
            # count contains the number of rows that are exactly the same or exactly opposite of the current row
            # why are we interested in this? 
            # because when we flip the required cols to make our current row to either all 0s or all 1s
            # then a row exactly similar to us will also become all 0s or all 1s
            # and a row exactly opposite to us will become all 0s or all 1s
            # for example
            '''
            100 --> current row
            011 --> opposite to current row
            100 --> same as current row
            101 --> different from current row
            here if we are currently in row 1, ie, 100
            flip is 011, ie, row 2
            so if we flip our first col,
            row1 --> 000
            row2 --> 111
            row3 --> 000
            row4 --> 001
            so here, by doing our flip of col 1 which makes us 000, rows similar to us, ie, row3 also becomes 0.
            rows opposite to us, ie, row2 also becomes 111
            note nothing happens to row4 after transformation, it is still not 000 or 111
            Hence, we are interested in rows same or opposite.
            '''
            for k in range(rows):
                if matrix[i] == matrix[k] or flip == matrix[k]:
                    count +=1
            
            ans = max(ans, count)
        return ans
    
    def solve2(self, matrix):
        dic = collections.Counter()
        for row in matrix:
            # cannot do dic[row] because lists are unhashable
            # hence, convert to tuple
            dic[tuple(row)] +=1
            flip = [1-x for x in row]
            dic[tuple(flip)] +=1
            
        maxVal = 1
        for k in dic.keys():
            if dic[k] > maxVal:
                maxVal = dic[k]
        return maxVal
        
        
    