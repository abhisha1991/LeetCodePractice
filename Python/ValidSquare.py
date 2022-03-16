# https://leetcode.com/problems/valid-square
class Node:
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]


class Solution:
    # note that taking square is better than sqrt because we can avoid unnecessary sqrt computation, larger squared dist is equivalent to larger sqrt dist
    # and most importantly, "square of integer diff" added to other "square of integer diff" will result in integer only
    # this cannot be said for square root values since they may be float if you take sqrt
    # this is a problem, because we cannot compare 2 float numbers for equality which we later do when checking for square criteria
    def sqDist(self, p1, p2):
        return (p1.x-p2.x)**2 + (p1.y-p2.y)**2

    # here n1, n2 and n3 are already squared values
    # so no need to square again
    def checkPyth(self, n1, n2, n3):
        return n3 == n1+n2

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [Node(p1), Node(p2), Node(p3), Node(p4)]
        result = []
        # just an arr of 0-4
        idx = [i for i in range(len(points))]

        # note that we're doing range up to n-1
        # we can do range up to n as well, just that the last point doesn't need 
        # validation if the other 3 are already validated
        for p in range(len(points)-1):
            # other points except for the current one
            other = [points[x] for x in idx if x!=p]
            
            d1 = self.sqDist(points[p], other[0])
            d2 = self.sqDist(points[p], other[1])
            d3 = self.sqDist(points[p], other[2])

            if d1 == 0 or d2 == 0 or d3 == 0:
                return False
            
            if d1 != d2 and d2 != d3 and d1 != d3:
                return False
            
            # if 2 sides match and 3rd side matches pythagorous criteria
            # then that point is a valid one in terms of being part of a square
            if d1 == d2 and self.checkPyth(d1, d2, d3):
                result.append(True)
                continue
            
            if d2 == d3 and self.checkPyth(d2, d3, d1):
                result.append(True)
                continue
            
            if d3 == d1 and self.checkPyth(d3, d1, d2):
                result.append(True)
                continue
            
            # if none of the above criterias matched, then this point is not a square
            result.append(False)
        
        for p in result:
            if not p:
                return p
        
        return True