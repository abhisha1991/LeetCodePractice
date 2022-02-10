from collections import defaultdict
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
# basically this is an application of level order traversal printing line by line

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def __init__(self):
        self.level = 0
        self.q = []
        # key is level, value is list of nodes in that level
        self.nodes_by_level = defaultdict(list)
        
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return
        
        self.q.append(root)
        # none signifies end of level
        self.q.append(None)
        self.bfs()
        
        # do the linking of nodes by level, given that we have nodes by level
        for level, node_list_in_level in self.nodes_by_level.items():
            # notice how we're doing to range n-1, because the last node is linked to nothing always!
            for i in range(len(node_list_in_level)-1):
                # previous node (left) in tree view is linked to next node in same level (next right neighbor)
                node_list_in_level[i].next = node_list_in_level[i+1]
        
        # notice how we're returning the tree root
        # this is because the dic nodes_by_level and its internal list node_list_in_level 
        # contain references to the tree nodes so the linking has been established there on the same objects 
        # so it is safe to return the tree
        return root
    
    def bfs(self):
        while len(self.q) > 0:
            # get first item
            item = self.q.pop(0)
            
            if item is not None:
                # add list of nodes at a given level, in order left to right
                self.nodes_by_level[self.level].append(item)
                
                # add valid children to queue
                if item.left is not None:
                    self.q.append(item.left)
                if item.right is not None:
                    self.q.append(item.right)
            else:
                # if item is None, level end has been reached
                self.level +=1
                # THIS IS VERY CLEVER - this ensures that we do the level order traversal
                # take an example of [1,2,3,4,5,6,7] to convince yourself that after "1" we add a "None" intentionally to signify end of level containing [2,3]
                self.q.append(None)
            
            # break out of infinite loop, else we will keep adding None as per line 61
            if len(self.q) == 1 and self.q[0] is None:
                break