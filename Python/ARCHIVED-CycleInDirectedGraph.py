# http://www.geeksforgeeks.org/?p=18516
# Look at the other file, much more intuitive

# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices
from collections import defaultdict

white = []
grey = []
black = []
flag = True
global_graph = defaultdict(list)


def is_cyclic(n, graph):
    global white
    global flag
    global black
    global grey
    global global_graph
    if flag:
        global_graph = graph
        fill_white_set()
    flag = False
    result = False
    while len(black) < n:
        if len(set(grey)) != len(grey):
            result = True
            break
        if len(grey) == 0:
            if len(white) > 0:
                unvisited = white.pop()
                grey.append(unvisited)
            else:
                # in case the graph itself is disconnected
                result = False
                break
        if unvisited in black:
            grey.remove(unvisited)
            if len(grey) > 0:
                unvisited = grey[-1]
            continue
        if len(global_graph[unvisited]) == 0:
            black.append(unvisited)
            grey.remove(unvisited)
            if len(grey) > 0:
                unvisited = grey[-1]
        elif black_contains_graph_ele(global_graph[unvisited]):
            black.append(unvisited)
            grey.remove(unvisited)
            if len(grey) > 0:
                unvisited = grey[-1]
        else:
            ele = find_nbor_ele(unvisited)
            grey.append(ele)
            unvisited = ele

    return result


def black_contains_graph_ele(eles):
    for i in eles:
        if i not in black:
            return False
    return True


def find_nbor_ele(unvisited):
    eles = global_graph[unvisited]
    for i in eles:
        if i not in black:
            return i
    return None


def fill_white_set():
    for k, v in global_graph.items():
        white.append(k)


t = int(input())
for i in range(t):
    ve = [int(x) for x in input().strip().split(' ')]
    edges = [int(x) for x in input().strip().split(' ')]
    if len(edges) % 2 == 1:
        raise AttributeError("Error in input for edges")
    j = 0
    e = defaultdict(list)
    src = -1
    dst = -1
    for i in edges:
        if j % 2 == 0:
            src = i
            j += 1
        else:
            dst = i
            j += 1
        if j >= 2 and j % 2 == 0:
            e[src].append(dst)

    x = is_cyclic(ve[0], e)
    print(x)