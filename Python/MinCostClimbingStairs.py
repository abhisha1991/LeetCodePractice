# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # steps is the total num of steps to climb
        steps = len(cost)-1        
        n = len(cost)
        
        minCost = dict()
        # this is so that cost[n] is defined as 0, else we'll get an out of bounds error on line 20
        # when evaluating n
        cost.append(0)
        
        def helper(num):
            if num < 0:
                return 0
            
            if num in minCost:
                return minCost[num]
            
            # incur cost of step + additional costs of either taking 1 step or 2 steps
            minCost[num] = cost[num] + min(helper(num-1), helper(num-2))
            return minCost[num]
        
        helper(n)
        return min(minCost[steps], minCost[n])
        