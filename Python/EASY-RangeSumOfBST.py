#https://leetcode.com/problems/range-sum-of-bst/

class Solution:
    ans = 0
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.dfs(root,L,R,0)

    def dfs(self,root,L,R,ans):
        if not root:
            return self.ans
        if L<=root.val<=R:
            self.ans+=root.val
        self.ans = self.dfs(root.left,L,R,self.ans)
        self.ans = self.dfs(root.right,L,R,self.ans)

        return self.ans
