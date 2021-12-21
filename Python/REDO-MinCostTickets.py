# https://leetcode.com/problems/minimum-cost-for-tickets/submissions/
class Solution(object):
    def __init__(self):
        self.dp = dict()
        self.days = []
        self.costs = []
        
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        self.days = days
        self.costs = costs
        self.helper(1)
        return self.dp[1]
    
    def helper(self, i):
        # optimization in dictionary keys
        if i in self.dp.keys():
            return self.dp[i]
        
        # constraint, i <= 365, if it is > 365, cost is 0 as we dont travel beyond 365 days
        if i > 365:
            self.dp[i] = 0
        
        # i is a "travel day", then decide cheapest pass to buy for next n days
        elif i in self.days:
            self.dp[i] = min(self.helper(i+1) + self.costs[0], \
                            self.helper(i+7) + self.costs[1], \
                            self.helper(i+30) + self.costs[2])
        # i is not a travel day, then defer to the next day
        else:
            self.dp[i] = self.helper(i+1)
            
        return self.dp[i]