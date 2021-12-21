from collections import defaultdict

# This solves 2 problems - finding cycle in directed graph and topological sort
# https://leetcode.com/problems/course-schedule-ii/description/
# this applies 2 separate concepts - good question
class Solution:
    def __init__(self):
        self.edges = defaultdict(list)
        self.visited = []
        self.res = []
        self.recstack = []

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # building the graph itself
        for i in prerequisites:
            if i[1] not in self.edges:
                self.edges[i[1]] = [i[0]]
            else:
                self.edges[i[1]].append(i[0])

        self.visited = [False] * numCourses
        self.recstack = [False] * numCourses
        print("edges are", self.edges)
        # if there's a cycle in the graph, then no courses can be recommended
        if self.hascycle(numCourses):
            return []

        # re-init visited array
        self.visited = [False] * numCourses

        for i in range(numCourses):
            if self.visited[i] == False:
                self.topsort(i)

        return list(reversed(self.res))

    def hascycle(self, numCourses):
        for i in range(numCourses):
            if self.visited[i] == False:
                if self.iscycle(i):
                    return True
        return False

    def iscycle(self, v):
        self.visited[v] = True
        self.recstack[v] = True

        for j in self.edges[v]:
            if self.visited[j] == True and self.recstack[j] == True:
                return True
            else:
                if self.iscycle(j):
                    return True

        self.recstack[v] = False
        return False

    def topsort(self, parent):
        self.visited[parent] = True

        for child in self.edges[parent]:
            if self.visited[child] is False:
                self.topsort(child)

        self.res.append(parent)
