# https://leetcode.com/problems/possible-bipartition
# https://www.youtube.com/watch?v=0ACfAqs8mm0
from collections import defaultdict
class Solution:
    def __init__(self):
        self.res = True
    
    # we need to create a bipartite graph
    # bipartite graph is one in which the vertices can belong to one of 2 sets u and v,
    # u and v are disjoint and every edge of graph connects a vertex in u to a vertex in v
    # dislike = [[1,2], [2,3], [2,4], [3,5], [4,5]] can be partitioned into 2 sets u and v
    # u = [1, 3, 4], v = [2, 5]
    '''
            U      V
         == 1 --/- 2 (notice 1,2 are connected "across" u,v)
         |  3 -/-- 5 (notice 3,5 are connected "across" u,v)
         == 4 /____| (notice 4,2 are connected "across" u,v)
                     (notice 4,5 are connected "across" u,v) etc.
            
            if we had an additional point, say [1,4] in dislike
            we would have to connect "within" the same set U (shown in left part of diagram) -- this would violate the definition of a bipartite graph
    '''
    # bipartite graph can only have even edge length cycle, not odd edge length cycle
    # even edge length cycle can be detected through vertex coloring of a graph with 2 colors (where no 2 vertices adjacent to each other share same color)
    # so to show a graph is bipartite we try to do 2 color vertex coloring ==> to imply that we have an even edge length cycle
    # if we're able to do this, we can obtain a bipartite graph ==> and since we can obtain bipartite graph, we can separate (partition) the nodes into 2 sets u,v
    # see video if this piece is unclear 
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        notlike = defaultdict(list)
        
        for d in dislikes:
            notlike[d[0]].append(d[1])
            # dislike is a 2 way street
            notlike[d[1]].append(d[0])
        
        for i in range(1, n+1):
            if i not in notlike:
                notlike[i] = []
        
        # note that blue = opposite of red and vice versa, ie, red = -blue and blue = -red
        blue = 1
        red = -1
        unassigned = 0
        
        # color dictionary - person i is colored with either blue or red
        # our goal is to color everyone and not have 2 nodes next to each other be the same color
        # if we can achieve this, then we return true, else false
        color = dict()
        
        # set all nodes to unassigned initially
        for nl in notlike:
            color[nl] = unassigned
        
        visited = set()
        def dfs(node, c):
            if node in visited:
                return
            
            visited.add(node)
            color[node] = c
            for nbr in notlike[node]:
                # your neighbor is colored the same as you, so this is not good!
                if color[nbr] == c:
                    self.res = False
                    break
                else:
                    # try and color neighbor with opposite of your own color
                    # ie, if current node is red, attempt to color blue on nbr
                    # and vice versa
                    dfs(nbr, -c)
        
        # do dfs for all non visited nodes
        # in case you have a disconnected graph, your dfs will only be run on partial graph
        # if you don't do for loop on all nodes
        for i in range(1, n+1):
            if i not in visited:
                dfs(i, red)
        
        r = []
        b = []
        
        for k,v in color.items():
            if v == red:
                r.append(k)
            if v == blue:
                b.append(k)
                
        print(f"group red is... {r}")
        print(f"group blue is... {b}")
        
        return self.res