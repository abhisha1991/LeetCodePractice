#https://leetcode.com/problems/range-sum-of-bst/

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.dfs(root,L,R,0)

    def dfs(self,root,L,R,cur_sum):
        if not root:
            return cur_sum
        if L<=root.val<=R:
            cur_sum+=root.val
        l_sum = self.dfs(root.left,L,R,cur_sum)
        r_sum = self.dfs(root.right,L,R,l_sum)

        return r_sum
