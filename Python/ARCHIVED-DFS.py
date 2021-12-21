# https://www.youtube.com/watch?v=iaBEKo5sM7w
# This is O(n2),better method is here: http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/
class DFS(object):
    def __init__(self, nodes, edges, start):
        self.stack = list()
        self.visited = list()
        self.nodes = nodes
        self.edges = edges
        self.start = start

    def dfs(self):
        self.stack.append(self.start)
        self.visited.append(self.start)
        while len(self.stack) > 0:
            nbors = self.find_unvisited_nbors(self.stack[len(self.stack) - 1])
            if len(nbors) == 0:
                self.stack.pop()
            else:
                first_nbor = nbors[0]
                self.stack.append(first_nbor)
                self.visited.append(first_nbor)

        print(self.visited)

    def find_unvisited_nbors(self, item):
        result = []
        for i in edges:
            if item == i[0]:
                if i[1] not in self.visited:
                    result.append(i[1])

            elif item == i[1]:
                if i[0] not in self.visited:
                    result.append(i[0])

        return result

nodes = [0, 1, 2, 3, 4, 5, 6, 7]
edges = [(0, 1), (1, 2), (1, 3), (2, 3), (0, 4), (2, 4), (4, 5), (4, 6), (5, 7)]
start = 0
dfss = DFS(nodes, edges, start)
dfss.dfs()

print("Another test")
nodes = [0, 1, 2, 3, 4, 5]
# disconnected graph, 5 is not connected
'''
0 --1--4 5
|  /|
| / |
2/ -3
'''
edges = [(0, 1), (1, 2), (1, 3), (2, 0), (2, 3), (1, 4)]
start = 0
dfss = DFS(nodes, edges, start)
dfss.dfs()

print("Another test")
nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8]
edges = [(0, 1), (1, 8),
         (8, 2), (2, 3),
         (8, 6), (2, 5),
         (6, 5), (2, 4),
         (6, 7), (4, 7)]

start = 0
dfss = DFS(nodes, edges, start)
dfss.dfs()

