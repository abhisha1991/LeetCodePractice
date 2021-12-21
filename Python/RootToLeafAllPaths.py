# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://www.youtube.com/watch?v=zIkDfgFAg60
# combo of inorder and stack
class Solution(Object):
    stack = []

    def rootToLeafAllPaths(self, root):
        if root == None:
            return
        
        self.push(root.val)
        self.rootToLeafAllPaths(root.left)
        if (root.left == None and root.right == None):
            print(Solution.stack)
            
        self.rootToLeafAllPaths(root.right)
        self.pop()

    def push(self, val):
        Solution.stack.append(val)
    
    def pop(self):
        Solution.stack = Solution.stack[0:len(Solution.stack)-1] 