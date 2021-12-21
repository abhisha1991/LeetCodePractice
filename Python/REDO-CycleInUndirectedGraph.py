# https://www.youtube.com/watch?v=n_t0a_8H8VY
from collections import defaultdict

visited = []
ggraph = defaultdict(list)


'''
G4G function
'''
def isCyclic(n, graph):
    global ggraph
    ggraph = graph
    cycle_in_undirected_graph(n, graph)

'''
My main function
'''
def cycle_in_undirected_graph(n, graph):
    global visited
    visited = [False] * n
    for i in range(n):
        if visited[i] is False:
            if is_cycle(i, graph, 0):
                return True
    return False


def is_cycle(v, graph, parent):
    global visited
    visited[v] = True
    # https://www.youtube.com/watch?v=n_t0a_8H8VY excellent explanation (part 2 using DFS)
    # pass parent in each iteration, find all nbors except parent [the direction where you're coming from]
    # if any of these nbors have been already visited, it means there was 1 edge involving that "nbor"
    # Now you are trying to connect "v" [YOURSELF] to that "nbor" again, means there is a cycle
    nbors = [x for x in graph[v] if x != parent]
    for i in nbors:
        if visited[i] is True:
            return True
        else:
            if is_cycle(i, graph, v):
                return True

    return False


def add_edge(u, v):
    if v not in ggraph[u] and u != v:
        ggraph[u].append(v)
        ggraph[v].append(u)

add_edge(0, 1)
add_edge(0, 3)
add_edge(0, 2)
add_edge(1, 2)
add_edge(3, 4)
'''
1 -- 0 -- 3 -- 4
|  /
| /
 2
'''
x = cycle_in_undirected_graph(5, ggraph)
print(x)

ggraph = defaultdict(list)
add_edge(0, 4)
add_edge(1, 2)
add_edge(1, 3)
add_edge(2, 3)
add_edge(2, 4)
add_edge(4, 5)
add_edge(4, 6)
add_edge(5, 7)
x = cycle_in_undirected_graph(8, ggraph)
print(x)

ggraph = defaultdict(list)
add_edge(0, 0)
x = cycle_in_undirected_graph(1, ggraph)
print(x)

ggraph = defaultdict(list)
add_edge(9,19)
add_edge(29,31)
add_edge(10,72)
add_edge(57,73)
add_edge(2,19)
add_edge(62,67)
add_edge(83,70)
add_edge(24,78)
add_edge(16,16)
add_edge(59,56)
add_edge(75,9)
add_edge(2,26)
add_edge(26,55)
add_edge(43,19)
add_edge(5,42)
add_edge(66,54)
add_edge(17,51)
add_edge(1,28)
add_edge(79,58)
add_edge(57,81)
add_edge(33,35)
add_edge(20,73)
add_edge(62,44)
add_edge(23,78)
add_edge(17,82)
add_edge(7,8)
add_edge(8,9)
add_edge(74,74)
add_edge(64,73)
add_edge(9,69)
add_edge(32,75)
add_edge(80,5)
add_edge(82,81)
add_edge(73,77)
add_edge(12,3)
add_edge(30,45)
add_edge(38,51)
add_edge(74,56)
add_edge(51,14)
add_edge(7,24)
add_edge(12,14)
add_edge(32,60)
add_edge(63,23)
add_edge(50,43)
add_edge(12,60)
add_edge(68,0)
add_edge(7,64)
add_edge(46,6)
add_edge(18,35)
add_edge(39,70)
add_edge(38,70)
add_edge(71,33)
add_edge(77,62)
add_edge(45,0)
add_edge(76,8)
add_edge(25,44)
add_edge(62,13)
add_edge(21,41)
add_edge(76,71)
add_edge(40,45)
add_edge(3,25)
add_edge(45,11)
add_edge(45,47)
add_edge(57,19)
add_edge(39,52)
add_edge(5,33)
add_edge(78,77)
add_edge(22,71)
add_edge(11,68)
add_edge(28,3)
add_edge(32,53)
add_edge(3,11)
add_edge(66,24)
add_edge(52,59)
add_edge(52,9)
add_edge(60,11)
add_edge(74,61)
add_edge(62,75)
add_edge(25,35)
add_edge(11,64)
add_edge(44,56)
add_edge(13,38)
add_edge(49,76)
add_edge(26,16)
add_edge(60,10)
add_edge(59,8)
add_edge(63,63)
x = cycle_in_undirected_graph(84, ggraph)
print(x)