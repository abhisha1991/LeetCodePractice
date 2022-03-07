'''
        0/1
        /  \
       /    \
    1/2     2/2
    /  \       \
   /    \       \
3/1     4/1      5/1

A sewer drainage system is structured as a tree. 
Water enters the system at n nodes numbered from 0 to n-1 and flows through the tree to the root, which has the number 0. 
The tree structure is defined by an array parent, where parent[i] = j means that water flows from node i to its direct parent node j. 
Water exits the system after it flows through the root, so the root has no parent, represented as parent[0] = -1. 
The value in input[i] denotes the amount of water that enters the serwer system at node i. 
This excludes water that flows into i from its children. 
The total flow through a node is thus the flow that enters at that node, plus the sum of the total flows of all of its children.

Your task is to divide the system into two smaller pieces by cutting one branch so that the total flows of the resulting subtrees are as close as possible.

Example

parent = [-1, 0, 0, 1, 1, 2]

input = [1, 2, 2, 1, 1, 1]

The structure of the system is shown in the diagram above. The nodes labeled as <node number>/<input flow>.

Solution for above tree:

Cut the branch between nodes 1 and 0.
The partition {0, 2, 5} has the flow input[0] + input[2] + input[5] = 1 + 2 + 1 = 4.
The partition {1, 3, 4} has the flow input[1] + input[3] + input[4] = 2 + 1 + 1 = 4.
So the difference between these 2 flows is 4-4 = 0
This is the closest possible difference, so we need to return this "difference value", ie, 0

if there was any other cut, say between nodes 0 and 2, 
then the 2 sub trees formed would have been {0, 1, 3, 4} and {2, 5}, so the difference of flows would be (1 + 2 + 1 + 1) - (2 + 1) = 2
This difference is MORE than the earlier one, so its not the minimum, so we cannot cut here

!!! Asked in 2 sigma initial round !!!
Answer inspired from here: https://github.com/dangermike/sewer
'''
import math
from collections import defaultdict

def getChildrenMap(parent):
    # dictionary with key = parent id, and value = list of children
    # in the graph above, this will contain an entry for children[1] = [3,4]
    children = defaultdict(list)
    
    for i in range(len(parent)):
        # reached condition of root, so there is no parent for this
        if parent[i] == -1:
            continue
        
        # establish parent and child, writing extra variable for clarity
        p = parent[i]
        c = i
        children[p].append(c)
    
    return children

def getTotalSubInflowsHelper(inputs, parent, children, subInflows, idx):
    for c in children[idx]:
        subInflows[idx] += getTotalSubInflowsHelper(inputs, parent, children, subInflows, c)
    return subInflows[idx]

def getTotalSubInflows(inputs, parent):
    children = getChildrenMap(parent)
    # so far sub inflows is just what is flowing through that node natively (for every node)
    # we need to find the total sub inflows, such that we are adding children flows to this array
    subInflows = inputs
    # start with 0 index, ie, root node
    # below helper function is recursive, such that it will handle all its children recursively
    # it applies dfs
    getTotalSubInflowsHelper(inputs, parent, children, subInflows, 0)
    return subInflows

def getMinDiff(inputs, parent):
    print()
    print("inputs is {0}".format(inputs))
    print("parent is {0}".format(parent))
    
    cutIndex = -1 # invalid cut index, will be updated every iteration in for loop
    cutScore = math.inf # final value to return, originally, set to invalid value, will be updated in for loop below
    if len(inputs) == 0 or len(parent) == 0:
        return cutScore
    
    # there cannot be a parent of the root, per the question
    if parent[0] != -1:
        return cutScore

    # can only cut at the root, so return updated cutScore
    if len(parent) == 1:
        cutScore = inputs[0]
        return cutScore
    
    # get total sub inflows for every node
    subInflows = getTotalSubInflows(inputs, parent)
    print("subInflows is {0}".format(subInflows))

    totalInflow = subInflows[0] # contains total flow of the sewer going through the root
    halfTotalInflow = totalInflow/2 # half of above value, we want to cut at a point so that we are able to reach a value close to this
    
    # find min cutScore by cutting at every node in the tree and seeing if you're able to reach a lower cut score
    for i in range(len(parent)):
        score = abs(halfTotalInflow - subInflows[i])
        print("Assuming we cut at index {0}, we get a score of {1}".format(i, score))
        if score < cutScore:
            cutScore = score
            cutIndex = i
    
    return cutScore, cutIndex

# main run time
parent = [-1, 0, 0, 1, 1, 2]
inputs = [1, 2, 2, 1, 1, 1]
print(getMinDiff(inputs, parent))


parent = [-1, 0, 0, 1, 1, 3, 4, 3, 5, 7]
inputs = [9, 1, 9, 7, 3, 5, 5, 1, 6, 6]
print(getMinDiff(inputs, parent))