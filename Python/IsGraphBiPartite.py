# https://leetcode.com/problems/is-graph-bipartite/
from collections import defaultdict
class Solution:
    def __init__(self):
        self.res = True
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # our final graph is 'g'
        # we need to re-form the graph since the v to u edges are not given in the input
        g = defaultdict(list)
        maxnode = 0
        
        for u, listv in enumerate(graph):
            g[u] = listv
            
            maxnode = max(maxnode, u)
            for v in listv:
                g[v].append(u)
                maxnode = max(maxnode, u, v)
                
        # for bipartite, we do graph coloring algorithm with 2 colors
        # ie, is it possible to assign each vertex a color (blue or red) such that
        # blue vertex is never next to red vertex and vice versa
        # if this is possible, graph is bipartite
        # https://www.youtube.com/watch?v=0ACfAqs8mm0
        blue = 1
        red = -blue
        unassigned = 0
        color = dict()
        
        for k in range(0, maxnode + 1):
            color[k] = unassigned
        
        def dfs(n, c):
            # if graph node is already colored with right color
            # then no action needed
            if color[n] == c:
                return
            
            # if node is colored with a color you're not intending it be colored with
            # then graph is not bipartite
            if color[n] == -c:
                self.res = False
                return
            
            # color node n with color c
            color[n] = c
            
            # go into neighbors of n, and attempt to color them with opposite color
            for nbor in graph[n]:
                dfs(nbor, -c)
        
        # do dfs on all unvisited (unassigned color nodes)
        # why? cos graph could be disconnected
        # so if we only did dfs(node=0), then we may only partially do dfs without exploring 
        # other disconnected sub-graphs
        for i in range(maxnode+1):
            if color[i] == unassigned:
                dfs(i, blue)
        
        return self.res