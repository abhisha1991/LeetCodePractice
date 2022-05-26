# https://leetcode.com/problems/bus-routes
from collections import defaultdict
from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        if source == target:
            return 0
        
        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].append(bus)
        
        
        # the q contains a tuple of 2 elements (stop to explore, current set of buses we have been on)
        q = deque([(source, set())])
        # if we've already explored a stop, we add to this set
        stopVisited = set()
        # if we've already explored a bus, we add to this set
        busVisited = set()
        
        while q:
            stop, bset = q.popleft()
            
            if stop == target:
                # return length of buses we have onboarded so far
                return len(bset)
            
            stopVisited.add(stop)
            
            for b in graph[stop]:
                if b in busVisited:
                    continue
                    
                busVisited.add(b)
                
                # add this new bus to take to a new set
                bsetNew = set(bset)
                bsetNew.add(b)
                # explore all stops for this bus
                for s in routes[b]:
                    if s not in stopVisited:
                        q.append((s, bsetNew))
        return -1