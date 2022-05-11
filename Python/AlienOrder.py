# https://leetcode.com/problems/alien-dictionary/
from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        
        # add a set for each char of each word in words
        # to capture its neighbors
        # we use a set instead of a list because we want only unique dependencies
        for w in words:
            for c in w:
                graph[c] = set()
        
        # why -1? because we want tp go through every pair of words - w1 and w2 till the end 
        # this is building our graph
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            
            # if w1 is longer than w2 when their prefix are the same, 
            # then w1 should be coming after (lexicographically) compared to w2
            # so we have an invalid ordering, so return early
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                # find first non matching char and add a dependency from w1 char to w2 char
                # example, w1 = 'wrt' and w2 = 'wrf'
                # they will mismatch at j==2, so we want to a directed dependency from t --> f
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        res = []
        # false in visited means, we have visited the node but its not in current path
        # true in visited means, we have visited the node and it is in current path
        visited = dict()
        
        # this is doing topological sorting
        def dfs(n):
            if n in visited:
                return visited[n]
            
            visited[n] = True
            for nbor in graph[n]:
                if dfs(nbor):
                    return True
                
            # not in current path anymore
            visited[n] = False
            # add to reverse, but in opposite order
            res.append(n)
        
        for c in graph:
            # cycle detection
            if dfs(c):
                return ""
        
        # no cycle so far
        # res holds result in opposite order (topological sort)
        res.reverse()
        return "".join(res)