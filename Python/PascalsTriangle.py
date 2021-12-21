# https://leetcode.com/problems/pascals-triangle/submissions/
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        res = [[1], [1,1]]
        arr = [1,1]
        while len(res) < numRows:
            i, j = 0, 1
            tmp = [arr[0], arr[-1]]
            while j < len(arr):
                s = arr[i] + arr[j]
                tmp.insert(i+1, s)
                i +=1
                j +=1
            res.append(tmp)
            arr = copy.copy(tmp)
            
        return res