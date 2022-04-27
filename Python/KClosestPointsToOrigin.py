# https://leetcode.com/problems/k-closest-points-to-origin/
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return x**2 + y**2
        
        h = []
        heapq.heapify(h)
        
        # has a mapping of the points corresponding to a distance key
        # for example, dist = 1 can be true for points [1,0] and [0,1]
        # so dmap[1] = [[1,0], [0,1]]
        dmap = defaultdict(list)
        
        for p in points:
            d = dist(p[0], p[1])
            dmap[d].append(p)
            
            # only minheap is implemented in python
            # whereas we want a max heap so we can kick out the max values from the heap if size of heap > k
            heapq.heappush(h, -d)
            if len(h) > k:
                mx = heapq.heappop(h)
                
                # only minheap is implemented in python
                mx = -1 * mx
                
                # kick out furthest dist point from the dmap
                if mx in dmap:
                    if len(dmap[mx]) > 1:
                        # if there are multiple points x dist away, kick out the first one 
                        dmap[mx] = dmap[mx][1:]
                    else:
                        del dmap[mx]
        
        res = []
        visited = set()
        while h:
            x = heapq.heappop(h)
            x = -1 * x
            
            # if we have visited a point, then don't re-evaluate, else you'll have duplicate entry in res
            # example, k=2 and points = [[0,1], [1,0]]
            if x in visited:
                continue
                
            res.extend(dmap[x])
            
            visited.add(x)
            
        return res