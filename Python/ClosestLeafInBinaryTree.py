# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        
        if root.left is None and root.right is None:
            return root.val
        
        # create a parent to child dictionary
        # holds parent of a node
        '''
            1
           / \
          2   3
          
        ie, parent[3] = 1
        '''
        parent = dict()
        def helper(node, p):
            if not node:
                return
            
            parent[node] = p
            helper(node.left, node)
            helper(node.right, node)
            
        
        helper(root, None)
        
        
        # holds all parents of k till the root
        # order is important, 
        # 1st element will be immediate parent
        # 2nd element will be grand parent
        # 3rd element will be great grand parent etc.
        parentsK = []
        kNode = None
        for n in parent:
            if n.val == k:
                # if k itself is a leaf, we can early return
                # since the closest "leaf" to k is k itself
                if n.right == None and n.left == None:
                    return n.val
                
                # collect all parents (ancestors) of k
                p = parent[n]
                while p:
                    parentsK.append(p)
                    p = parent[p]
                
                # have a ref to the k node as well
                kNode = n
                break
        
        def getMinDistToLeaf(node):
            if not node:
                return sys.maxsize
            
            if node.left == None and node.right == None:
                return 0
            
            # returns min dist from node to any of its leaves
            return 1 + min(getMinDistToLeaf(node.left), getMinDistToLeaf(node.right))
        
        
        # specialized version of above function
        # along with min dist being returned, it also holds a bunch of leaves and their dist from that node
        '''
                1
               / \
              2   3
             / \
            4   5
           /
          6
        
        Say node = 2, then this will return [(6,2), (5,1)]
        basically, leaf "6" is 2 dist away from node "2" and leaf "5" is 1 dist away from node "2"
        '''
        def getMinDistToLeafWithMetadata(node, d, leafs):
            if not node:
                return sys.maxsize
            
            if node.left == None and node.right == None:
                leafs.append((node.val, d))
                return 0
            
            return 1 + min(getMinDistToLeafWithMetadata(node.left, d+1, leafs), getMinDistToLeafWithMetadata(node.right, d+1, leafs))
        
        leafs = []
        # how much is the k node away from its leaves
        baseDist = getMinDistToLeafWithMetadata(kNode, 0, leafs)
        
        # holds the node to min leaf dist
        dists = [(kNode, baseDist)]
        
        # this distFromK is representing the dist of a parent from k
        # this will be 1 for the immediate parent
        # this will keep incrementing by 1 for every subsequent parent (ie, ancestor)
        # notice that array parentsK holds parents in youngest to oldest order (so we can do this increment by 1)
        distFromK = 1
        for p in parentsK:
            # parent may be connected to a short path to a leaf other than going through k
            # capture that dist in d
            d = getMinDistToLeaf(p)
            
            # we MUST reach k from the parent
            # this line is critical, since it is finding shortest paths from ancestors to their leaves
            # which dont pass through k, and then adding k to ensure we are connected to k
            '''
                        1
                       / \
                      2   3
                     /
                    4
                   /
                  5 
                 /
                6
               /
              7
             /
            8
            
            imagine k = 4
            parent[4] = 2
            parent[2] = 1
            parentsK = [2, 1]
            
            baseDist from node 4 is 4 (4 --> 5 --> 6 --> 7 --> 8)
            minDistToLeaf for parent 2 is 5 (leaf 8)
            minDistToLeaf for parent 1 is 1 (leaf 3)
            
            BUT we must add "distFromK" to each of parents so we can touch k node
            so dist to leaf touching k (for parent 2) = 5 + 1 = 6
            so dist to leaf touching k (for parent 1) = 1 + 2 = 3
            
            this is what we're doing below
            '''
            dists.append((p, d + distFromK))
            distFromK +=1
        
        dists = sorted(dists, key=lambda x: x[1])
        # get min dist to leaf node that touches k node and get its the leaf in "leafs"
        getMinDistToLeafWithMetadata(dists[0][0], 0, leafs)
        leafs = sorted(leafs, key=lambda x: x[1])
        
        # return the node that has the min dist to k
        return leafs[0][0]