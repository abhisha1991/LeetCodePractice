# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/flip-equivalent-binary-trees/ 
# https://leetcode.com/problems/flip-equivalent-binary-trees/solution/ 
'''
Time Complexity: O(min(M,N)) where M and N are number of nodes in each tree.
Reason: In worst case we need to check all the nodes, but untill we exhaust all the nodes of the minimum size tree.
Space Complexity: O(min(H1,H2)), where H1 and H2 are the height of trees or O(min(M,N)) in the worst case.
Reason: The space is need for the stack in recursion. In worst case a tree can be a single branch where the hight is equal to the size of the tree. Hence the space complexity can be O(min(M,N)) where M and N are number of nodes in each tree.
'''
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        root2 = self.flip(root2)
        return self.checkequal(root1, root2)
    
    def checkequal(self, r1, r2):
        if r1 == None and r2 == None:
            return True
        
        if r1 == None or r2 == None:
            return r1 == r2
        
        print("Going to compare " + str(r1.val) + " and " + str(r2.val))
        return r1.val == r2.val and (self.checkequal(r1.left, r2.left) and self.checkequal(r1.right, r2.right)) or \
        (self.checkequal(r1.left, r2.right) and self.checkequal(r1.right, r2.left))
    
    def flip(self, root2):
        if root2 == None:
            return None
        
        l = root2.left
        r = root2.right
        
        root2.left = r
        root2.right = l
        print("after flipping, root2 is" + str(root2.val))
        if root2.left == None:
            print("after flipping, root2.left is None")
        else:
            print("after flipping, root2.left is " + str(root2.left.val))
        if root2.right == None:
            print("after flipping, root2.right is None")
        else:
            print("after flipping, root2.right is " + str(root2.right.val))
        self.flip(root2.left)
        self.flip(root2.right)
        
        return root2
