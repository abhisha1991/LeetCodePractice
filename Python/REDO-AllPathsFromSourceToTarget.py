# https://leetcode.com/problems/all-paths-from-source-to-target/solution/
from collections import defaultdict

class Solution(object):
    
    graphdic = defaultdict(list)
    result = []
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        lastNode = len(graph) - 1
        self.createGraph(graph, lastNode)
        self.dfs(0, lastNode, [0])
        return Solution.result
        
    def createGraph(self, graph, lastNode):
        for i in range(0, lastNode):
            for j in graph[i]:
                Solution.graphdic[i].append(j)
    
    def dfs(self, start, end, path):    
        if start == end:
            Solution.result.append(path)
        for s in Solution.graphdic[start]:
            self.dfs(s, end, path + [s])
            