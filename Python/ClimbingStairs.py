# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        # key is total steps, value is total num ways of reaching those steps
        steps = dict()
        steps[0] = 0
        steps[1] = 1 # only 1 way to do 1 step
        steps[2] = 2 # 2 ways to do 2 steps (1+1) or (2)
        
        if n in steps:
            return steps[n]
        
        def helper(num):
            if num in steps:
                return steps[num]
            
            steps[num] = helper(num-2) + helper(num-1)
            return steps[num]
        
        helper(n)
        return steps[n]