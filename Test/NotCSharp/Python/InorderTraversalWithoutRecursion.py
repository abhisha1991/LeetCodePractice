# section 9.7 of EPI - implement non recursive version
# https://leetcode.com/problems/binary-tree-inorder-traversal/
def inorder(tree):
    stack = []
    res = []

    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.left # go left
        else:
            tree = stack.pop()
            res.append(tree.val) # print node
            tree = tree.right # go right
    return res

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

print(inorder(None))
print(inorder(TreeNode(1)))

# below tree
x = TreeNode(1)
x.left = TreeNode(2)
x.right = TreeNode(3)
x.left.left = TreeNode(4)
x.left.right = TreeNode(5)
print(inorder(x))

'''
    1
   / \
  2   3
 / \
4   5

4 2 5 1 3
'''