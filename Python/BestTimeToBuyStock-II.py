# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        profit = 0
        
        while i < len(prices):
            # greedy approach, keep buying on one day and selling the next day and take profits off the table whenever you can
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
            i +=1
            
        return profit