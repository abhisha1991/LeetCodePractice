# asked in pure storage
# given n (x,y) points in coordinate plane, return maximum number of squares possible
import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Solution():
    def __init__(self, points):
        # we are making points as float because they are forced to be float post rotation (rotatep2)
        # so if we don't make it float, it will cause problems during comparison (arePointsSame)
        self.points = [Point(p[0] * 1.0, p[1] * 1.0) for p in points]
        # creating a dictionary for o(1) lookup
        self.dic = {}
        
        # note that tuples can be hashed as keys, so can 'Point' objects
        # BUT notice the below difference on why we add tuples as keys
        '''
        d = dict()
        d[(1,2)] = 0
        (1,2) in d --> returns True

        p = Point(1,2)
        d[p] = 0
        Point(1,2) in d --> returns False
        This is because the dictionary is holding the object p 
        whereas we're asking if a new Point (another object) is in dictionary, thus false
        '''
        for p in self.points:
            # value doesn't matter
            self.dic[(p.x, p.y)] = 0
    
    # rotates point p2 about point p1
    def rotatep2(self, p1, p2, angle, verbose=False):
        s = math.sin(math.radians(angle))
        c = math.cos(math.radians(angle))
        s = round(s, 3)
        c = round(c, 3)

        if verbose:
            print(f"Transforming p2 {p2.x},{p2.y} by degrees: {angle} around p1 {p1.x},{p1.y}")

        # create a new copy of p2
        p2 = Point(p2.x, p2.y)

        # translate p2 to origin
        p2.x -= p1.x
        p2.y -= p1.y 

        # rotate p2 getting new x,y
        xnew = p2.x * c - p2.y * s
        ynew = p2.x * s + p2.y * c 

        # translate back p2 about p1
        p2.x = xnew + p1.x
        p2.y = ynew + p1.y

        if verbose:
            print(f"Transformed point new is (p2.x)= {p2.x}, (p2.y)= {p2.y}")

        return p2
    
    def printPoints(self, points):
        for p in range(len(points)):
            print(f"Idx: {p}, x={points[p].x} and y={points[p].y}")

    # inspired from https://github.com/abhisha1991/LeetCodePractice/blob/master/Python/ValidSquare.py
    # this is o(1) operation since there are guaranteed 4 points we're calculating
    def isSquare(self, points):
        if len(points) < 4:
            return False
        
        def sqDist(p1, p2):
            return (p1.x - p2.x)**2 + (p1.y - p2.y)**2 

        def checkPyth(n1, n2, n3):
            return n1 + n2 == n3
        
        if type(points[0]) != Point:
            print("Warning - converting tuples to points...")
            points = [Point(p[0], p[1]) for p in points]

        arr = []
        for p in range(len(points)):
            other = [i for i in range(4)]
            other.remove(p)
            d1 = sqDist(points[p], points[other[0]])
            d2 = sqDist(points[p], points[other[1]])
            d3 = sqDist(points[p], points[other[2]])

            if d1 == 0 or d2 == 0 or d3 == 0:
                return False
            
            if d1 != d2 and d1 != d3 and d2 != d3:
                return False

            if d1 == d2 and checkPyth(d1, d2, d3):
                arr.append(True)
                continue
            
            if d2 == d3 and checkPyth(d2, d3, d1):
                arr.append(True)
                continue            
            
            if d1 == d3 and checkPyth(d1, d3, d2):
                arr.append(True)
                continue

            arr.append(False)

        if False in arr:
            return False
        return True

    def arePointsSame(self, p, q):
        if p.x == q.x and p.y == q.y:
            return True
        return False

    # this method is used for getting points p3 and p4 in o(1) time each
    def getTransformPointList(self, p, q):        
        # get 2 points rotating 2nd point by 90 degrees around 1st point
        # these are potential points - a and b
        a = self.rotatep2(p, q, 90)
        b = self.rotatep2(p, q, -90)
        point_list = []

        # finding new point is o(1)
        if self.arePointsSame(a, p) or self.arePointsSame(a, q) or (a.x, a.y) not in self.dic:
            if self.arePointsSame(b, p) or self.arePointsSame(b, q) or (b.x, b.y) not in self.dic:
                # neither of the 2 potential points are a valid 3rd point
                return point_list
        else:
            # we know at least 'a' is a valid 3rd point
            point_list = [a]
            # lets check for 'b' again
            if self.arePointsSame(b, p) or self.arePointsSame(b, q) or (b.x, b.y) not in self.dic:
                pass
            else:
                # both points are potential valid third points
                point_list.append(b)

        return point_list

    def countSquares(self):
        squares = set()
        for p1 in self.points:
            for p2 in self.points:
                if self.arePointsSame(p1, p2):
                    continue

                # anchor p1, rotate p2
                p3_list = self.getTransformPointList(p1, p2)
                # if we're unable to find 3rd point, iterate next
                if len(p3_list) == 0:
                    continue

                # notice that we can use the exact same method here that we used for p3 to find p4 (ie, rotate and check if it exists in dict)
                # so overall time complexity will be o(n2) implementing the efficient method for p3, p4
                for p3 in p3_list:
                    # anchor p3, rotate p1
                    p4_list = self.getTransformPointList(p3, p1)
                    for p4 in p4_list:
                        if self.arePointsSame(p4, p1) or self.arePointsSame(p4, p2) or self.arePointsSame(p4, p3):
                            continue
                        
                        sq = [p1, p2, p3, p4]
                        # need to sort for de-dupe
                        # treated as o(1) as the size of sq is const
                        sq = sorted(sq, key=lambda p: (p.x, p.y))
                        
                        if self.isSquare(sq):
                            # notice we're converting to tuple so we can utilize de-dupe in set during add
                            tups = (sq[0].x, sq[0].y, sq[1].x, sq[1].y, sq[2].x, sq[2].y, sq[3].x, sq[3].y)
                            len_sq = len(squares)
                            squares.add(tups)

                            # only print non duplicate squares
                            if len(squares) > len_sq:
                                self.printPoints(sq)
                                print("-" * 50)
            
        return len(squares)


'''
s = Solution([(0,0), (1,0), (1,1), (0,1), (2,0), (2,1)])
print(s.countSquares())
'''

s = Solution([(1,0)])
print(s.countSquares())

s = Solution([(1,1), (0,1), (2,0)])
print(s.countSquares())

s = Solution([(1,1), (0,1), (2,0), (3,0)])
print(s.countSquares())

s = Solution([])
print(s.countSquares())

s = Solution([(0,0), (1,0), (1,1), (0,1), (2,0), (2,1), (0,2), (1,2), (2,2)])
print(s.countSquares())

'''
s = Solution([(0,0), (1,0), (1,1), (0,1), (2,0), (2,1), (0,2), (1,2), (2,2), (-1,0), (-1,1), (-1,2)])
print(s.countSquares())
'''

'''
s = Solution([(0,0), (1,0), (1,1), (0,1), (2,0), (2,1), (0,2), (1,2), (2,2), (-1,0), (-1,1), (-1,2), (-1,-1), (0,-1), (1,-1), (2,-1)])
print(s.countSquares())
'''