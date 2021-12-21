# http://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/
# Same as word search problem in c# section
from collections import defaultdict

visited = defaultdict()


def boggle(matrix, words, rows, cols):
    result = []

    for w in words:
        start = w[0]
        # find all possible positions of the first letter of the word
        pos = find_pos(matrix, start, rows, cols)
        if len(pos) == 0:
            continue
        for p in pos:
            # initialize all visited positions to false
            initialize_visited(rows, cols)
            visited[p] = True
            # check if the word exists, if yes, then add it to result
            r = find_word(w[1:], matrix, p, rows, cols)
            if r is True:
                result.append(w)

    if len(result) == 0:
        return []

    final_result = []
    for i in result:
        if i not in final_result:
            final_result.append(i)

    return list(sorted(final_result))


def find_word(partial_w, matrix, p, rows, cols):
    if len(partial_w) == 0:
        return True
    start = partial_w[0]
    # get valid neighbors
    nbors = get_nbors(p, matrix, rows, cols)
    # if there are multiple positions where start is present, record it here
    possible_i = []
    res = False
    for i in nbors:
        # if the current matrix element is start and we haven't visited the node
        if matrix[i[0]][i[1]] == start and visited[i] is False:
            visited[i] = True
            # add it to the potential list of starting points
            possible_i.append(i)
            # this is the stopping condition
            if len(partial_w) == 1:
                return True
    # try all possible searches from the positions collected
    for ii in possible_i:
        res = res or find_word(partial_w[1:], matrix, ii, rows, cols)
        # if unsuccessful in finding the word, back track and mark those positions as false
        # for the full understanding of this, try searching 'SEEK' in the example provided in G4G
        if res is False:
            visited[ii] = False

    return res


def initialize_visited(rows, cols):
    for i in range(rows):
        for j in range(cols):
            p = (i, j)
            visited[p] = False

# get all valid neighbors, neighbors whose points go beyond the edge, don't count


def get_nbors(p, matrix, rows, cols):
    nbors = []
    n = []
    n.append((p[0] - 1, p[1]))
    n.append((p[0] + 1, p[1]))
    n.append((p[0], p[1] + 1))
    n.append((p[0], p[1] - 1))
    n.append((p[0] - 1, p[1] + 1))
    n.append((p[0] - 1, p[1] - 1))
    n.append((p[0] + 1, p[1] + 1))
    n.append((p[0] + 1, p[1] - 1))
    for i in n:
        if i[0] < 0 or i[0] >= rows or i[1] < 0 or i[1] >= cols:
            continue
        else:
            nbors.append(i)
    return nbors

# find all possible positions which have the character 'start' in them


def find_pos(matrix, start, rows, cols):
    result = []
    for i in range(0, rows):
        for j in range(0, cols):
            if matrix[i][j] == start:
                result.append((i, j))
    return result


t = int(input())
for i in range(t):
    n = int(input())
    words = [x for x in input().strip().split(' ')]
    nm = [int(x) for x in input().strip().split(' ')]
    letters = [x for x in input().strip().split(' ')]
    matrix = []
    z = 0
    for j in range(0, nm[0]):
        temp = []
        for k in range(0, nm[1]):
            temp.append(letters[z])
            z += 1
        matrix.append(temp)
    result = boggle(matrix, words, nm[0], nm[1])
    ans = ''

    for i in result:
        ans = ans + i + ' '
    if ans == '':
        ans = '-1'
    print(ans.strip())

