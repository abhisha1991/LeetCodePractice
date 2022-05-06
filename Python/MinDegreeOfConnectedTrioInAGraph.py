# https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:        
        
        connected = [[0] * (n+1) for i in range(n+1)]
        indegree = dict()
        
        for i in range(1, n+1):
            indegree[i] = 0
                
        for a,b in edges:
            # undirected means both way connection
            
            connected[a][b] = 1
            connected[b][a] = 1
            
            indegree[a] += 1
            indegree[b] += 1

        minTrioDegree = sys.maxsize
        cycleFound = False
        
        for c1 in range(1, n+1):
            # this optimization is important - notice how c2 is starting at c1 + 1 
            for c2 in range(c1 + 1, n+1):
                # if c1 and c2 are not connected, don't bother going into c3 level
                if not connected[c1][c2]:
                    continue
                
                # this optimization is important, notice how c3 is starting at c2 + 1
                # this implies that we're consdering fewer combinations compared to all going from (1, n+1)
                for c3 in range(c2 + 1, n+1):
                    if connected[c1][c3] and connected[c2][c3]:
                        cycleFound = True
                        
                        # notice how we have the indegree of the trio as total in degree -6
                        # why? if 'a' is connected to [b,c] amongst others, 
                        # 'b' is connected to [a,c] amongst others
                        # 'c' is connected to [a,b] amongst others
                        # we have 6 connections within the trio, we need only outer connections 
                        triodegree = indegree[c1] + indegree[c2] + indegree[c3] - 6
                        if minTrioDegree > triodegree:
                            minTrioDegree = triodegree
                        
        if not cycleFound:
            return -1
        
        return minTrioDegree