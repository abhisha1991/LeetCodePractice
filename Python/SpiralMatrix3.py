# read the solution explanation, not code for: https://leetcode.com/problems/spiral-matrix-iii/ 

class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        # east, south, west, north
        # column - row - column - row
        
        # walk is 1, 1, 2, 2, 3, 3, 4, 4 etc.
        
        res = []
        step = 1
        count = 1
        res.append([r0,c0])
        if R * C == 1: return res
        while R * C > len(res):
                # go east
                for j in range(0, step):
                    c0 = c0 + 1
                    if self.checkinrange(R, C, r0, c0):
                        res.append([r0, c0])
                
                # go south
                for i in range(0, step):
                    r0 = r0 + 1
                    if self.checkinrange(R, C, r0, c0):
                        res.append([r0, c0])
                        
                # increment step by 1, as walk is 1,1 then 2,2 etc.
                step +=1
                
                # go west
                for j in range(step, 0, -1):
                    c0 = c0 - 1
                    if self.checkinrange(R, C, r0, c0):
                        res.append([r0, c0])
                
                # go north
                for i in range(step, 0, -1):
                    r0 = r0 - 1
                    if self.checkinrange(R, C, r0, c0):
                        res.append([r0, c0])
                
                # increment by 1, as walk is 2,2 then 3,3
                step +=1
                
        return res
        
    def checkinrange(self, R, C, i, j):
        if i >=0 and i < R and j>=0 and j < C:
            return True
        return False
            