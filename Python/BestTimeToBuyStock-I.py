# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = sys.maxsize
        n = len(prices)
        l = 0
        while l < n:
            if low > prices[l]:
                low = prices[l]
            
            profit = max(profit, prices[l]-low)
            l +=1
        
        return profit