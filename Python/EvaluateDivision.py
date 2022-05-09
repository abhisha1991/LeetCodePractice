# https://leetcode.com/problems/evaluate-division/
from collections import defaultdict
class Solution:
    def __init__(self):
        self.res = []
        
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            v = values[i]
            
            graph[a].append((b, v))
            graph[b].append((a, 1/v))
            
        
        def dfs(node, dest, r, idx):
            if node == dest:
                self.res[idx] = r
                return
            
            if node in visited:
                return
            
            visited.add(node)
            
            for child in graph[node]:
                n = child[0]
                val = child[1]
                dfs(n, dest, r * val, idx)
            
        
        # initialize res explicitly to invalid values
        # if it evaluates as a valid value, it will be set as part of dfs run
        self.res = [-1] * len(queries)
        
        for i in range(len(queries)):
            # reset visited after every query run
            visited = set()
            q = queries[i]
            
            # if either query key is not in graph, then its not a valid query, so assign -1
            if q[0] not in graph or q[1] not in graph:
                self.res[i] = -1
                continue
            
            # if both keys are same, then div must be 1, so set to 1
            # note the order of this if condition, must happen after above if condition
            if q[0] == q[1]:
                self.res[i] = 1
                continue
            
            dfs(q[0], q[1], 1, i)
            
        return self.res