# https://leetcode.com/problems/number-of-provinces/
from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)
        
        # create adjacency graph
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    graph[i].append(j)
                    
        visit = [False] * n

        def dfs(i):
            visit[i] = True
            for g in graph[i]:
                if visit[g] == False:
                    dfs(g)

        # final result    
        count = 0
        for i in range(n):
            if visit[i] == False:
                dfs(i)
                # after full dfs we have found 1 connected component (province)
                count +=1
        
        return count