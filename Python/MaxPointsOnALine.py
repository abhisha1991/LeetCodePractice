# https://leetcode.com/problems/max-points-on-a-line
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 1:
            return 0
        
        if n == 1:
            return 1
        
        mx = 0
        
        def getSlope(x1, y1, x2, y2):
            if x1 == x2:
                return sys.maxsize
                
            return (y2-y1) / (x2-x1)
        
        for i in range(n):
            dic = defaultdict(int)
            # why reset the dictionary at every iteration?
            # (0,0), (1,1), (0,1), (1,2), (2,3)
            # imagine if you have these points, there are 2 parallel lines formed:
            # [(0,0), (1,1)] and [(0,1), (1,2), (2,3)] - both have slope 1, ans should be 3 points, ie, [(0,1), (1,2), (2,3)] 
            
            
            # now if we consider point x1,y1 as 0,0 - then we get dic[1] = 1, ie, its slope calculation with point (1,1)
            # now imagine if we didn't reset the dictionary after processing point (0,0)
            # note that when we process (1,1) its not going to consider (0,0), it will look only from i+1 to n (inner for loop)
            
            # next we process point (0,1) - for this point, it will form the slope 1 with points (1,2) and (2,3)
            # if we didn't clear the dictionary, it will make dic[1] = 3, which is not correct since we added to global freq
            # for all lines having slope 1, and didn't consider them to be separate lines
            for j in range(i+1, n):
                s = getSlope(points[i][0], points[i][1], points[j][0], points[j][1])
                dic[s] +=1
                mx = max(mx, dic[s])
            
        # why return mx+1
        # consider example of [[0,0], [1,1]] - after processing point (0,0) - we have dic[1] = 1, but there are actually 2 pts
        # who are on the same line. (0,0) was not added to freq because it was being used as the reference point to calc slope
        return mx+1