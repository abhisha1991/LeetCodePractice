# https://leetcode.com/problems/student-attendance-record-ii
# https://www.youtube.com/watch?v=D5g-KZWbh6Y
class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        # innermost to outermost 3 d array
        # 3rd dimension represents either 0 or 1 (thus range(2)) - which represents absent/not absent
        # why are we considering only 0 or 1 absent? since 2 or more absent is an invalid criteria
        
        # 2nd dimension represents either 0,1,2 (thus range(3)) - which represents 0,1,2 consecutive lates
        # why are we considering only 0,1,2 consecutive lates? since 3 or more consecutive lates is an invalid criteria
        
        # 1st dimension (outermost) represents 0 to n+1, ie, including 'n' in dp
        # our result will be a summation of dp[n][consecutiveLate][absent]
        # ie, it will be dp[n][0][0] + dp[n][0][1] + dp[n][1][0] + dp[n][1][1] + dp[n][2][0] + dp[n][2][1]      
        dp = [[[0 for i in range(2)] for j in range(3)] for k in range(n+1)]
        
        # BASE CASE
        
        # length 1, 0 consecutive lates, 0 or 1 absent
        dp[1][0][0] = 1 # P
        dp[1][0][1] = 1 # A
        
        # length 1, 1 consecutive lates, 0 or 1 absent
        dp[1][1][0] = 1 # L
        dp[1][1][1] = 0 # N/A (not possible to have string length 1 with 1 late and 1 absent)
        
        # length 1, 2 consecutive lates, 0 or 1 absent
        dp[1][2][0] = 0 # N/A (not possible to have string length 1 with 2 consecutive lates)
        dp[1][2][1] = 0 # N/A (not possible to have string length 1 with 2 consecutive lates and 1 absent)
    
        # for any integer i, it is ONLY possible to have 6 states
        # as given below, this is because problem constraints us to having 0,1,2 consecutive lates
        # and 0,1 absents -- thus giving us 3 x 2 = 6
        for i in range(2, n+1):
            dp[i][0][0] = (dp[i-1][0][0] + dp[i-1][1][0] + dp[i-1][2][0]) % mod
            dp[i][0][1] = (dp[i-1][0][0] + dp[i-1][1][0] + dp[i-1][2][0] + dp[i-1][0][1] + dp[i-1][1][1] + dp[i-1][2][1]) % mod

            # example, we were at i-1=2 with 0 consecutive lates, no absent and we want to reach 1 consecutive late with no absent
            # example: if we had "PP" and now we go to "PPL"
            # example: if we had "LP" and now we go to "LPL" (remember consecutive late resets to 0)
            dp[i][1][0] = dp[i-1][0][0] % mod

            # example, we were at i-1=2 with 0 consecutive lates, 1 absent and we want to reach 1 consecutive late with 1 absent
            # example: PA --> PAL
            # example: AP --> APL 
            dp[i][1][1] = dp[i-1][0][1] % mod

            # example, we were at i-1=3 with 1 consecutive lates, 0 absent and we want to reach 2 consecutive late with 0 absent
            # example: PPL --> PPLL
            dp[i][2][0] = dp[i-1][1][0] % mod

            # example, we were at i-1=3 with 1 consecutive lates, 1 absent and we want to reach 2 consecutive late with 1 absent
            # example: APL --> APLL
            # example: PAL --> PALL
            dp[i][2][1] = dp[i-1][1][1] % mod
        
        
        return (dp[n][0][0] + dp[n][0][1] + dp[n][1][0] + dp[n][1][1] + dp[n][2][0] + dp[n][2][1]) % mod

    # this is correct and easier to understand, but gives TLE, even though we are caching
    def checkRecord2(self, n: int) -> int:
        mod = 10**9 + 7
        self.cache = dict()
        
        self.cache[0] = 0
        
        def dfs(n, remaining, consecutiveLate, hasAbsent):
            if remaining == 0:
                return 1
            
            if remaining in self.cache:
                return self.cache[remaining]
            
            tmp = 0
            # if student is not absent so far, 1 absent is allowed
            # note that consecutive late resets to 0 when we are adding an 'absent'
            if not hasAbsent:
                tmp += dfs(n, remaining-1, 0, True) % mod
            
            # add to consecutive late only if current lates that are consecutive are < 2
            if consecutiveLate < 2:
                tmp += dfs(n, remaining-1, consecutiveLate+1, hasAbsent) % mod
            
            # add for student being 'present', always
            # note that consecutive late resets to 0 for this case
            tmp += dfs(n, remaining-1, 0, hasAbsent) % mod
            self.cache[n] = tmp % mod
            
            return tmp
        
        dfs(n, n, 0, False)
        return self.cache[n]