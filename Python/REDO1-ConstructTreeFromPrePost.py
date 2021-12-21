# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/solution/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        N = len(pre)
        if N == 0:
            return None
        root = TreeNode(pre[0])
        if N == 1:
            return root
        
        # len of pre is 2 or more
        L = post.index(pre[1]) + 1
        # left branch gets only left elements populated into it
        root.left = self.constructFromPrePost(pre[1:L+1], post[0:L])
        # right branch gets only right elements populated into it
        root.right = self.constructFromPrePost(pre[L+1:N], post[L:N-1])
        return root

'''
Consider the example given in the solution

Output: [1,2,3,4,5,6,7]


        1
      /   \
     2     3
    / \   / \
   4   5 6   7

Input: 
pre = [1,  "2",4,5,  3,6,7], 

post = [4,5,"2",  6,7,3,  1]

focus on element 2, head element of the left tree  - note all elements are unique in the problem definition
notice that 2 is pre[1], also notice that there are 3 elements in the left tree
notce that 2 is post[3-1], or post[number of elements in left tree - 1] or post[L-1]

In the array "pre"
notice that left tree is [1:L+1] ==> [2,4,5]
notice that right tree is [L+1:N]

In the array "post"
notice that left tree is [0:L]
notice that right tree is [L:N-1], why N-1? because last element, ie, N is the root node "1"

let's generalize with another example:

Output: [1,2,3,4,5,6,7,8,9]


        1
      /   \
     2     3
    / \   / \
   4   5 6   7
  / \ 
 8   9

pre = [1,  "2",4,8,9,5,  3,6,7], 

post = [8,9,4,5,"2",  6,7,3,  1]

again, lets focus on 2 - the head of the left branch
notice, 2 = pre[1], in this case, number of elements in left branch are 5, ie, L=5
notice, 2 = post[4], or post[L-1]

for pre
notice, left tree, pre[1:L+1] = [2,4,8,9,5] and right tree = pre[L+1:N] = [3,6,7]

for post
notice, left tree = post[0:L] = [8,9,4,5,2] and right tree = post[L:N-1] = [5:8] = [6,7,3]

'''