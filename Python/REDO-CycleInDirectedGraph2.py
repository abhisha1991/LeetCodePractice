# http://www.geeksforgeeks.org/?p=18516
# This is an extension of DFS, we keep a rec_stack as well here

# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices
# https://leetcode.com/problems/course-schedule/description/

from collections import defaultdict

visited = []
rec_stack = []
ggraph = defaultdict(list)


def isCyclic(n, graph):
    global visited
    global rec_stack
    global ggraph
    visited = [False] * n
    rec_stack = [False] * n
    ggraph = graph
    # handles disconnected graphs as well!! [Try doing only "return is_cyclic(0)" for the 2nd example below]
    for i in range(n):
        if visited[i] is False:
            if is_cyclic(i):
                return True
    return False


def is_cyclic(v):
    global visited
    global rec_stack
    global ggraph
    visited[v] = True
    rec_stack[v] = True

    # traverse all nbors of node
    for j in ggraph[v]:
        # main condition for cycle - "rec_stack[j] is True" meaning there is a back edge to "j"
        # Try a simple 0 --> 1 --> 2 vs 0 --> 1 --> 2 --> 0 as an example
        if visited[j] is True and rec_stack[j] is True:
            return True
        else:
            if is_cyclic(j):
                return True

    # once you have traversed all nbors, then remove node from rec_stack
    # note that the node is STILL visited!
    rec_stack[v] = False
    return False

x = defaultdict(list)
x[0] = [1]
x[1] = [2]
x[2] = [3]
print(isCyclic(4, x))

x = defaultdict(list)
x[0] = [1]
x[1] = []
x[2] = [2]
print(isCyclic(3, x))

