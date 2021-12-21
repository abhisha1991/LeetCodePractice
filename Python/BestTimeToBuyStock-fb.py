# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        minele = prices[0]
        profit = 0
        for i in range(n):
            if prices[i] < minele:
                minele = prices[i]
        
            if prices[i] - minele > profit:
                profit = prices[i] - minele
        
        return profit