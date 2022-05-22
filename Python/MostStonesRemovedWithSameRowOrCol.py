# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        total = len(stones)
        groups = 0
        visited = set()
        
        def dfs(r,c):
            visited.add((r,c))
            self.groupRows.add(r)
            self.groupCols.add(c)
            
            for s in stones:
                if (s[0], s[1]) not in visited and (s[0] in self.groupRows or s[1] in self.groupCols):
                    dfs(s[0], s[1])
        
        for s in stones:
            i = s[0]
            j = s[1]
            if (i,j) not in visited:
                self.groupRows = set()
                self.groupCols = set()
                dfs(i, j)
                groups +=1

        # num stones on the board - num stones that we can't remove = number of stones that we can remove
        # number of stones we can't remove is given by the number of "groups" of stones that are "together"
        # together here means that they share the same row/col, 
        # so in effect, we need to find the number of groups of stones, ie, number of islands 
        
        # why are number of stones we can't remove == number of groups?
        # because for the last stone of that group, you won't be able to remove it since you need at least 1 other stone
        # who shares the same row/col
        return total - groups