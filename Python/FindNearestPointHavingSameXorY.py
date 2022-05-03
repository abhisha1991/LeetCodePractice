# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
from collections import defaultdict
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist = defaultdict(list)
        
        for p in range(len(points)):
            if points[p][0] == x or points[p][1] == y:
                d = abs(points[p][0]-x) + abs(points[p][1]-y)
                dist[d].append(p)
        
        minD = sys.maxsize
        idx = -1
        for k,v in dist.items():
            if minD > k:
                minD = k
                idx = dist[k][0]
        
        return idx