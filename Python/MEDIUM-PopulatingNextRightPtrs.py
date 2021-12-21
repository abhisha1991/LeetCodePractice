# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

from collections import defaultdict
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
# basically this is an application of level order traversal printing line by line

class Solution:
    def __init__(self):
        self.level = 0
        self.dic = defaultdict(list)
        self.q = []

    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        self.q.append(root)
        self.q.append(None)
        self.bfs(root)
        for k, v in self.dic.items():
            for i in range(len(v) - 1):
                v[i].next = v[i + 1]

    def bfs(self, root):
        if root == None:
            return

        while len(self.q) > 0:
            first = self.q[0]
            if first is None:
                self.level += 1
                self.q = self.q[1:]
                self.q.append(None)
            else:
                if first.left != None:
                    self.q.append(first.left)
                if first.right != None:
                    self.q.append(first.right)
                self.q = self.q[1:]

                if self.level not in self.dic.keys():
                    self.dic[self.level] = []

                self.dic[self.level].append(first)

            if len(self.q) is 1 and self.q[0] is None:
                break
'''
public class Solution {
    public void connect(TreeLinkNode root) {
        if(root == null || root.left == null) return;
        connectNodes(root.left, root.right);
    }
    
    public void connectNodes(TreeLinkNode node1, TreeLinkNode node2) {
        node1.next = node2;
        if(node1.left != null) {
            connectNodes(node1.right, node2.left);
            connectNodes(node1.left, node1.right);
            connectNodes(node2.left, node2.right);
        }
    } 
}
'''