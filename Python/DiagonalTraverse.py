# https://leetcode.com/problems/diagonal-traverse/
from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        
        rows = len(mat)
        cols = len(mat[0])
        
        for i in range(rows):
            for j in range(cols):
                '''
                for regular diagonal, r+c remains const
                imagine, 3x3 matrix, 
                so for top right element, r=0, c=2 (0+2 = 2)
                next element is r=1, c=1 (1+1 = 2)
                next element is r=2, c=0 (2+0 = 2)
                '''
                groups[i+j].append(mat[i][j])
        
        # even key will be in reverse order
        # odd key will be in natural order
        '''
            1  2  3
            4  5  6
            7  8  9

        dict_items([(0, [1]), (1, [2, 4]), (2, [3, 5, 7]), (3, [6, 8]), (4, [9])])
        
        expected output: [1, 2,4, 7,5,3, 6,8, 9]
                          r   s     r     s   r
        
        r = reversed order
        s = same order
        '''
        mxkey = max(groups.keys())
        ans = []
        for i in range(mxkey+1):
            elements = groups[i]
            if i % 2 == 0:
                elements = elements[::-1]
            ans.extend(elements)
        return ans