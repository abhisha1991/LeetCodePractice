# https://www.youtube.com/watch?v=ddTC4Zovtbc
# http://www.geeksforgeeks.org/topological-sorting/

# Function should return Topologically Sorted List
# Graph(graph) is a defaultict of type List
# n is no of edges
from collections import defaultdict


visited = list()
stack = list()
global_graph = None


def topoSort(n, graph):
    global global_graph
    global stack
    global visited
    stack = []
    visited = []
    global_graph = graph
    k = getUnvisitedKey()
    visited.append(k)
    while n != len(stack):

        curr = None
        for i in visited:
            if i not in stack:
                curr = i
                break

        if curr is None:
            k = getUnvisitedKey()
            visited.append(k)
            curr = k

        topoSortUtil(curr)

    result = list(reversed(stack))
    print(result)

    return result


def topoSortUtil(curr):
    children = findChildren(curr)
    if len(children) == 0:
        stack.append(curr)
        cleanupGraph(curr)
        return

    for c in children:
        if c in stack:
            continue
        grandChildren = findChildren(c)
        if c not in visited:
            visited.append(c)
        if len(grandChildren) == 0 and c not in stack:
            stack.append(c)
            cleanupGraph(c)
        else:
            topoSortUtil(c)


def cleanupGraph(c):
    for k, v in global_graph.items():
        if c in v:
            v.remove(c)


def findChildren(k):
    return global_graph[k]


def getUnvisitedKey():
    for k, v in global_graph.items():
        if k not in visited:
            return k
    return None

x = defaultdict(list)
x['a'] = ['c']
x['b'] = ['c', 'd']
x['c'] = ['e']
x['d'] = ['f']
x['e'] = ['h', 'f']
x['f'] = ['g']
x['g'] = []
x['h'] = []

topoSort(8, x)

x = defaultdict(list)
x['a'] = ['c']
x['b'] = ['c']
x['c'] = []
topoSort(3, x)

# ['b', 'a', 'c', 'e', 'd', 'f', 'g']
x = defaultdict(list)
x['a'] = ['c']
x['b'] = ['c', 'f']
x['c'] = ['g', 'd', 'e']
x['d'] = ['g']
x['e'] = ['f']
x['f'] = []
x['g'] = []
topoSort(7, x)

# same graph, diff order of default dict list
# ['b', 'a', 'c', 'e', 'd', 'f', 'g']
x = defaultdict(list)
x['a'] = ['c']
x['b'] = ['f', 'c']
x['c'] = ['e', 'd', 'g']
x['d'] = ['g']
x['e'] = ['f']
x['f'] = []
x['g'] = []
topoSort(7, x)