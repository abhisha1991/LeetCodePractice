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
        
        
        q = deque([(source, set())])
        visited = set()
        
        while q:
            stop, bset = q.popleft()
            
            if stop == target:
                return len(bset)
            
            visited.add(stop)
            
            for b in graph[stop]:
                bsetNew = set(bset)
                bsetNew.add(b)
                for s in routes[b]:
                    if s == target:
                        return len(bsetNew)
                    
                    if s not in visited:
                        q.append((s, bsetNew))
        return -1