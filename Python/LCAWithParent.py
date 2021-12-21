# section 9.4 of the EPI book.
# here we are given the parent of a node in a binary tree
# so we need to find the LCA
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None # this additional info is given for each node

def lcaWithParent(root, p, q):
    dic = dict()
    # enlist all parents for p
    while p != None:
        dic[p] = p.parent
        p = p.parent
    
    # starting at q, if any of the nodes of q or its ancestors are in the dictionary then that is the lowest common ancestor
    while q != None:
        if q in dic:
            return q.val
        q = q.parent

    return "ancestor not found!"
        

x = TreeNode(1)
x.left = TreeNode(2)
x.right = TreeNode(3)
x.right.right = TreeNode(4)
x.right.left = TreeNode(5)


x.left.parent = x
x.right.parent = x
x.right.right.parent = x.right
x.right.left.parent = x.right
'''
        1
       / \ 
      2   3
         / \
        5   4
'''

print(lcaWithParent(x, x.right.right, x.left)) # lca is root, ie, 1
print(lcaWithParent(x, x.right.right, x)) # lca is root, ie, 1
print(lcaWithParent(x, x.right.right, x.right.left)) # lca is root.right, ie, 3


