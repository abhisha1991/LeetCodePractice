# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
# https://www.youtube.com/watch?v=emF5eAYR3Nk
from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        # [[2,1],[3,4],[3,2]] is the input, whose answer is [1,2,3,4] or [4,3,2,1]
        # we do a graph formation - add u to v and add v to u
        '''
        1 --> 2
        2 --> 3,1
        3 --> 4,2
        4 --> 3
        '''
        for adj in adjacentPairs:
            graph[adj[0]].append(adj[1])
            graph[adj[1]].append(adj[0])
        
        '''
        notice that we need to now do a dfs from either 1 or from 4 (in the example above)
        these are our start points, which can be identified by being next to 1 (instead of 2) element(s)
        
        if we start a dfs from 1 (say), we get 1 --> 2 --> 3 --> 4, we keep adding the unvisited entries in our ans
        if we start a dfs from 4 (say), we get 4 --> 3 --> 2 --> 1

        if we start a dfs from 2 (say), we get 2 --> 3 --> 4 --> 1, which is incorrect
        '''
        start = -1
        for k,v in graph.items():
            if len(v) == 1:
                start = k
                break
        
        ans = []
        visited = set()
        def dfs(i):
            if i in visited:
                return
            
            ans.append(i)
            visited.add(i)
            
            for c in graph[i]:
                dfs(c)
    
        dfs(start)
        return ans