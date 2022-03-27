# https://leetcode.com/problems/paint-house-ii/
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        if n == 0 or k == 0:
            return 0
        
        # go through every house, start with idx 1 since we need h-1 access (prev house access)
        for h in range(1, n):
            # go through every color for present house
            for c in range(k):
                # get best cost from previous row
                # subject to constraint that current row cannot have same color as previous row
                # ie, prevC != c
                best = min([costs[h-1][prevC] for prevC in range(k) if prevC != c])
                    
                # note we're updating the costs arr itself, in place, so no extra space
                # so we've implicitly used memoization, not using an explicit dict
                # but by updating the costs arr itself
                costs[h][c] += best
        
        # the last row will contain the final costs as we paint from top to bottom
        return min(costs[-1])
    
    # no memoization occurs here, so simple dfs is not going to cut it
    # this is correct, but gets time limit exceeded
    def inefficient(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        arr = [sys.maxsize] * k
        
        if n == 0 or k == 0:
            return 0
        
        def helper(r, costSoFar, idx):
            # if we're at the end of our houses to paint
            if r >= n:
                return
            
            for c in range(k):
                # if some house above has already taken a lock on this paint
                # then we cant use this paint
                if r > 0 and costs[r-1][c] == '#':
                    continue
                
                paint = costs[r][c]
                
                # if we're going to be adding something larger than what's there in arr
                # we can skip since we already have a better solution
                if (paint + costSoFar) > arr[idx]:
                    continue
                
                # else paint, lock that color, incur cost
                costs[r][c] = '#'
                costSoFar += paint
                
                # if we've painted the last row house, then see if our overall costs
                # of painting are minimal than present value in arr
                # if so, then update arr for index i
                if r == n-1 and arr[idx] > costSoFar:
                    arr[idx] = costSoFar
                
                # and look into next hosue
                helper(r+1, costSoFar, idx)
                
                # back track, update costs[r][c] and be sure to subtract your "paint"
                # from cost so far, since we just temporarily painted 
                costs[r][c] = paint
                costSoFar -= paint
        
        # consider all options for painting house 0
        for i in range(k):
            helper(0, 0, i)
            
        return min(arr)