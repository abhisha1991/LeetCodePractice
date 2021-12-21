# taken from EPI - section 9.5
# sum ALL root to leaf paths of a binary tree whose nodes only have 0s or 1s.
'''
        1
       / \
      0   1
     / \
    1   0
Ans will be
101 + 100 + 11
5 + 4 + 3 = 12

need to do inorder traversal, why? because we want to count the root node first
'''
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sumpaths(root, total):
    if not root:
        return total
    
    total = 2*total + root.val
    # if its a leaf, return the sum
    if not root.left and not root.right:
        print("sum up to leaf is {0}".format(total))
        return total
    
    # if its a non leaf
    return sumpaths(root.left, total) + sumpaths(root.right, total)

x = TreeNode(1)
x.left = TreeNode(0)
x.left.left = TreeNode(1)
x.left.right = TreeNode(0)
x.right = TreeNode(1)

print(sumpaths(x, 0))