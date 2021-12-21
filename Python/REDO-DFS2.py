# http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/
# Applications of DFS: http://www.geeksforgeeks.org/?p=11644
# Good slides: optional reading http://ww3.algorithmdesign.net/handouts/DFS.pdf

from collections import defaultdict


class DFS(object):
    def __init__(self, n):
        self.src = 0
        self.dest = 0
        self.n = n
        self.graph = defaultdict(list)
        self.visited = [False] * self.n
        self.result = set()
        self.src_to_dst = False

    def dfs_traversal(self, src):
        self.src = src
        self.dfs_util(self.src)

    def dfs_search(self, src, dst):
        self.src = src
        self.dest = dst
        self.dfs_util2(self.src, self.dest)

    def dfs_util2(self, src, dest):
        self.visited[src] = True
        self.result.add(src)
        if dest in self.result:
            print("There is a path to ", dest)
            self.src_to_dst = True
            return

        for j in self.graph[src]:
            if self.visited[j] is False and self.src_to_dst is False:
                self.dfs_util2(j, dest)

    def dfs_util(self, i):
        self.visited[i] = True
        if len(self.result) == self.n:
            return

        self.result.add(i)

        for j in self.graph[i]:
            if self.visited[j] is False:
                self.dfs_util(j)

    def add_edge(self, i, j):
        if j not in self.graph[i]:
            self.graph[i].append(j)


dfss = DFS(5)
dfss.add_edge(0, 1)
dfss.add_edge(0, 2)
dfss.add_edge(0, 3)
dfss.add_edge(1, 2)
dfss.add_edge(2, 4)
dfss.add_edge(1, 1)

dfss.dfs_traversal(1)
print(dfss.result)

dfss = DFS(5)
dfss.add_edge(0, 1)
dfss.add_edge(0, 2)
dfss.add_edge(0, 3)
dfss.add_edge(1, 2)
dfss.add_edge(2, 4)
dfss.add_edge(1, 1)

dfss.dfs_search(1, 4)
print(dfss.result)

dfss = DFS(2)
dfss.add_edge(0, 1)
dfss.add_edge(1, 0)

dfss.dfs_traversal(0)
print(dfss.result)
