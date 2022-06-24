# https://leetcode.com/problems/binary-search-tree-iterator
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# this solution is o(n) size - gets accepted in Leetcode, but what if we want memory to be o(height)
# here we're just building the tree in the constructor, storing in arr and using counter to iterate
class BSTIterator2:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.counter = 0
        
        def helper(root):
            if not root:
                return
            
            helper(root.left)
            self.arr.append(root)
            helper(root.right)
        
        helper(root)
        self.n = len(self.arr)
            

    def next(self) -> int:
        val = self.arr[self.counter].val
        self.counter +=1
        return val

    def hasNext(self) -> bool:
        return self.counter < self.n

# this solution uses o(h) memory
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        # move leftward in tree and add all elements to the left of root
        while root:
            self.stack.append(root)
            root = root.left
        
    def next(self) -> int:
        # top of stack is the node we want to return
        node = self.stack.pop()
        # move 1 step right
        n = node.right
        # now do the exact same thing that we did in the constructor
        while n:
            self.stack.append(n)
            n = n.left
            
        return node.val

    def hasNext(self) -> bool:
        # if there are elements in stack, it returns true
        return self.stack

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()