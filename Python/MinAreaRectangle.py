# https://leetcode.com/problems/minimum-area-rectangle/
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        points = sorted(points, key=lambda t: (t[0], t[1]))
        pts = set()
        
        for p in points:
            pts.add((p[0], p[1]))
            
        ar = sys.maxsize
        for x1, y1 in points:
            for x2, y2 in points:
                # grab the diagonally opposite point (x2,y2) to the top right of x1,y1
                # example, say square is (1,1), (1,3), (3,3), (3,1)
                # so if x1,y1 is (1,1) then x2,y2 is (3,3) since x2 > x1 and y2 > y1
                if x2 <= x1 or y2 <= y1:
                    continue
                    
                width = abs(x2 - x1)
                # check if (1, 3) and (3, 1) are in points set
                if (x1, y2) in pts and (x2, y1) in pts:
                    height = abs(y2 - y1)
                    if width * height < ar:
                        ar = width * height
                    
        if ar == sys.maxsize:
            return 0
        return ar