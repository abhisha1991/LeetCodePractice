# https://leetcode.com/problems/maximum-number-of-points-with-cost
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows = len(points)
        cols = len(points[0])
        if rows == 0:
            return 0
        
        dp = points[0]
        if rows == 1:
            return max(dp)
        
        '''
        this is going to use dynamic programming
        say you calculated dp[i-1] as [d0, d1, d2, d3, d4, ..dj...dn]
        
        and now you want to calculate dp[i][j]
        so dp[i][j] = max(d0 - abs(j-0), d1 - abs(j-1), d2 - abs(j-2), ... dj - abs(j-j) ... dn - abs(j-n))
        or in general, 
        dp[i][j] = max(dk - abs(j-k)) for all k in cols
        
        now the problem is that if we need to iterate over rows x cols and for each row, we need to
        evaluate against all col elements of dp[i-1] and take max, 
        then that becomes rows x col^2 time complexity
        
        we want to keep a row x col time complexity
        
        try and evaluate dp[i][j-1] and compare against dp[i][j]
        say j = 4, then j-1 = 3
        
        dp[i][3] = max(d0-abs(3-0), d1-abs(3-1), d2-abs(3-2), d3-abs(3-3), d4-abs(3-4)...dn-abs(n-3))
        dp[i][3] = max(d0-3, d1-2, d2-1, d3-0, d4-1, d5-2, d6-3...dn-abs(n-3))
        vs
        dp[i][4] = max(d0-abs(4-0), d1-abs(4-1), d2-abs(4-2), d3-abs(4-3), d4-abs(4-4)...dn-abs(n-4))
        dp[i][4] = max(d0-4, d1-3, d2-2, d3-1, d4-0, d5-1, d6-2...dn-abs(n-4))
        
        look at the dp[i][3] vs dp[i][4] 
        we can say something like dp[i][j] = max(dp[i][j-1] - 1, dp[i-1][j]) for the left half up to d4
        
        we can do the exact same thing for rhs and make this into o(mn) time
        note below we use left/right to track parsing for a single row
        
        and instead of dp being 2d, its just 1d and gets updated for every row in place
        '''
        left = [0] * cols
        right = [0] * cols
        
        for i in range(1, rows):
            
            for j in range(cols):
                if j == 0:
                    left[j] = dp[j]
                else:
                    left[j] = max(left[j-1] - 1, dp[j])
            
            for j in range(cols-1, -1, -1):
                if j == cols-1:
                    right[j] = dp[j]
                else:
                    right[j] = max(right[j+1] - 1, dp[j])
            
            for j in range(cols):
                dp[j] = points[i][j] + max(left[j], right[j]) 
        
        return max(dp)