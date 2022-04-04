# idea for union find is to "union" and "find"
# this applies to graph problems for the most part (example, cycle detection in UNDIRECTED graph)
# https://www.youtube.com/watch?v=ayW5B2W9hfo
'''
     2---3
    / 
   0            4---5
    \
     1    

Say you're given this disjointed graph
Union find will help you do 2 things:
1. What set of nodes (group) does say node 1 belong to? (find)
2. Make group (4,5) belong to group (0,1,2,3) through a union operation
We'll write a program for defining the union find data structure

     2---3
    /   /
   0   /
    \ /
     1
This undirected graph has cycle, so we'll write a program to detect this using union find
'''
from collections import defaultdict
class Solution():
    def __init__(self, adjList):
        self.graph = defaultdict(list)
        # this is the mapping that tells you what group a given node belongs to
        # we choose a representative node to rep a group, say the first group is represented by 0
        # so parent[1] = 0, similarly, parent[3] = 2, but parent[2] = 0. Of course, parent[0] = 0, ie, the rep node is also its own parent
        self.parent = dict()

        # total number of nodes
        self.n = 0
        self.nodes = set()

        for adj in adjList:
            self.graph[adj[0]].append(adj[1])
            # dont do the below else a cycle condition will be detected
            # self.graph[adj[1]].append(adj[0])
            
            # keep inventory of all nodes in the set (duplicates are not added)
            self.nodes.add(adj[0])
            self.nodes.add(adj[1])
        
        self.n = len(self.nodes)
        self.makeSet()

    # make a disjointed set
    # every node in the graph is also its parent
    def makeSet(self):
        for i in range(self.n):
            self.parent[i] = i
    
    # find the root parent group of a given node
    def find(self, node):
        if self.parent[node] == node:
            return node
        
        return self.find(self.parent[node])
    
    def union(self, x, y):
        p1 = self.find(x) # find root parent of x
        p2 = self.find(y) # find root parent of y

        # make root_parent_y's parent be x's root parent
        # ie, make into a subtree of x's root parent, ie, union
        self.parent[p2] = p1
        '''

            n1          n4 ---n5
            / \
          n2   n3

        say we do union(n3, n4), we will get
        
            n1 --- n4 --- n5
            / \
          n2   n3
        '''

    def printGraph(self):
        print("printing graph...")
        for k,v in self.graph.items():
            print(f"for key: {k}, adjacency list is {v}")

    def detectCycle(self, verbose=False):
        if verbose:
            self.printGraph()

        for u, adj in self.graph.items():
            for v in adj:
                if verbose:
                    print(f"checking u: {u} and v: {v}")

                parent_u = self.find(u)
                parent_v = self.find(v)

                '''
                say you had 3 nodes like (0,1), (0,2), (1,2)
                       1
                     /  |
                    0   |
                     \ /
                      2
                this is a cycle we know, lets prove it

                iteration 1: consider node 0 in the for loop as u
                adj will be [1,2]
                    now consider u = 0, v = 1
                    parent_u = 0, parent_v = 1 --> diff, so we union them (0 -- 1), now parent_v = 0

                    now consider u = 0, v = 2
                    parent_u = 0, parent_v = 2 --> diff, so we union them, now parent_v = 0
                      1
                     / 
                    0   
                     \ 
                      2
                
                iteration 2: consider node 1 in the for loop as u
                adj will be [2], so v = 2
                parent_u = 0, parent_v = 0 --> same, thus cycle detected
                
                we are essentially building the graph, and saying that for any 2 nodes u,v which are connected (per adj list)
                if they have the same parent, then we know we are in a sitation like u,v connected to each other and common parent ==> cycle!
                '''

                if parent_u == parent_v:
                    print(f"cycle found! {u} and {v} are connected to common parent {parent_v}")
                    return True
                else:
                    if verbose:
                        print(f"parent_u: {parent_u} is different than parent_v: {parent_v}, going to union u and v")
                    
                    self.union(u, v)
                    
                    if verbose:
                        parent_u = self.find(u)
                        parent_v = self.find(v)
                        print(f"after union, parent_u: {parent_u} and parent_v: {parent_v}")
            
        print("cycle not found!")
        return False

### GRAPH CYCLE DETECTION ###
# test case 1
s = Solution([[0,1],[0,2],[2,3],[4,5]])
s.detectCycle()

# test case 2 - same input as test case 1, diff order of adj list
s = Solution([[0,1],[2,0],[2,3],[5,4]])
s.detectCycle()

# test case 3
s = Solution([[0,1],[0,2],[2,3],[1,3]])
s.detectCycle()

# test case 4 - same input as test case 3, diff order of adj list
s = Solution([[0,1],[2,0],[2,3],[3,1]])
s.detectCycle()

# test case 5
s = Solution([[0,1], [0,6], [0,7], [1,5], [2,3], [2,4], [10,11], [1,2], [7,8], [8,10], [8,9], [7,11]])
s.detectCycle(verbose=False)

### UNION/FIND FUNCTIONALITY ###
# this is the same graph as top of the page
s = Solution([[0,1],[0,2],[2,3],[4,5]])
s.union(0,1)
s.union(0,2)
s.union(2,3)
s.union(4,5)
print(f"root parent of 2 is {s.find(2)}")
print(f"root parent of 3 is {s.find(3)}")
print(f"root parent of 4 is {s.find(4)}")
print(f"root parent of 5 is {s.find(5)}")
print("performing union between group 0 and group 4")
s.union(0,5)
print(f"root parent of 4 is {s.find(4)}")
print(f"root parent of 5 is {s.find(5)}")