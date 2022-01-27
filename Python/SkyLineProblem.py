# https://leetcode.com/problems/the-skyline-problem
# https://www.youtube.com/watch?v=GSBLe8cKu0s
import heapq
from collections import defaultdict, OrderedDict

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if len(buildings) == 0:
            return None
        
        if len(buildings) == 1:
            b = buildings[0]
            return [[b[0], b[2]], [b[1], 0]]
        
        events = []
        for b in buildings:
            # b for beginning and e for end
            # intentionally chosen these words because we sort by this alphabet later
            # so this means we cannot do s (start) and e (end)
            events.append([b[0], b[2], 'b'])
            events.append([b[1], b[2], 'e'])
        
        # sort by x starting point
        # in case of tie on x axis, sort by 'beginning' then 'end' 
        # if still tied, sort by negative of height -- so that the tallest one comes first - we want to always process the tallest buildings first
        events = sorted(events, key=lambda x: (x[0], x[2], -x[1]))
        #print(events)
        
        output = []
        # by default, python has minheap only
        # so for maxheap -- we do multiplication by -1
        # we need max heap because we are tracking max building height at any given point in time
        maxheap = []
        heapify(maxheap)
        # init by pushing 0 to heap
        heappush(maxheap, 0)
        # currmax is the current highest building (negative) height in the skyline
        currmax = 0
        
        for e in events:
            negheight = -1 * e[1]
            if e[2] == 'b':
                heappush(maxheap, negheight)
                if currmax != maxheap[0]:
                    output.append([e[0], e[1]])
                    currmax = negheight
            elif e[2] == 'e':
                # https://stackoverflow.com/questions/5484929/removing-an-item-from-a-priority-queue
                maxheap.remove(negheight)
                heapify(maxheap)
                currmax = maxheap[0]
                if negheight < currmax:
                    output.append([e[0], -currmax])
        
        return self.ensureSingleEntry(output)
    
    # for a case like [[1,2,1],[1,2,2],[1,2,3]]
    # we need to return only [[1,3],[2,0]] instead of [[1,3],[2,2],[2,1],[2,0]]
    # so we need to post process the output
    def ensureSingleEntry(self, skyline):
        # notice we need an ordered dict because we need to maintain order (sorted by x axis value) in the answer 
        dic = OrderedDict()
        output = []
        for x in skyline:
            if x[0] in dic.keys():
                dic[x[0]].append(x[1])
            else:
                dic[x[0]] = [x[1]]
                
        for k,v in dic.items():
            if len(v) > 1:
                output.append([k, min(v)])
            else:
                output.append([k, v[0]])
        
        return output