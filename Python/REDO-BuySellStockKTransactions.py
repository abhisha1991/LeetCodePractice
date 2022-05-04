# https://www.youtube.com/watch?v=oDhu5uGq_ic
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        # rows are number of transactions - 0,1,2,...
        # cols are the days with corresponding prices, ie, prices[i] for ith day
        res = [[None] * len(prices) for i in range(k+1)]
        
        # 1st row is going to have 0 profit (since its k=0 transactions allowed)
        for i in range(len(prices)):
            res[0][i] = 0
        
        # 1st col is going to have 0 profit (since there is no sell date, only buy date)
        for i in range(k+1):
            res[i][0] = 0
        
        for i in range(1, k+1):
            for j in range(1, len(prices)):
                # we can choose not to transact, in which case we will have profits the same as prev day
                noTransact = res[i][j-1]
                
                # this maxdiff concept is just an optimization around 
                # considering if we want to transact on any of the m days, where m = 0 to j-1,
                # if we do transact on Mth day, then profit = price[j] - price[m] + res[i-1][m]
                # which is saying, that, we do the transaction (price[j] - price[m]) and then we add to this 
                # the state that we were in on the Mth day, one transaction row above (i-1)
                if j == 1:
                    maxDiff = res[i-1][0] - prices[0]
                else:
                    maxDiff = max(maxDiff, res[i-1][j-1] - prices[j-1])
                
                transact = maxDiff + prices[j]
                res[i][j] = max(transact, noTransact)
        
        return res[k][len(prices)-1]

    # non optimized version since we do the m=0 to j-1 calculation several times
    def maxProfit2(self, k: int, stocks: List[int]) -> int:
        len_stocks = len(stocks)
        arr = [[None] * len_stocks for x in range(k + 1)]

        for i in range(k + 1):
            for j in range(len_stocks):
                # i == 0 means that you are not allowed to make any transactions
                # - if this is the case, you can never make profit, hence arr[0][j] = 0
                # j == 0 means that you are at the starting day, you dont have any stock price of the past
                # this means you cannot do any trading, ie - you can buy only, and NOT sell, which means profit = 0
                if i == 0 or j == 0:
                    arr[i][j] = 0
                    continue

                maxi = 0
                tmpMaxi = 0
                dayPurchased = -1
                for m in range(j):
                    # m is the number of days from 0 to j-1
                    # if you decide to sell on day j for a stock you bought on day m, then profit from that sale is
                    # (price on day j - price on day m) + your earlier state [without making this transaction on day m]
                    x = stocks[j] - stocks[m] + arr[i-1][m]
                    # max always takes in an iterable! remember - hence we give a list below
                    # do max between earlier max, x and the result of doing no transaction arr[i][j-1]
                    # (same state as j-1 th day)
                    tmpMaxi = maxi
                    maxi = max([arr[i][j-1], x, tmpMaxi])
                    if maxi > tmpMaxi:
                        dayPurchased = m
                arr[i][j] = maxi
                # if your profit increased on that day - ie - you made a transaction, else you would be in prev state
                if arr[i][j] > int(arr[i][j-1]) and arr[i][j] != arr[i-1][j]:
                    print("Bought stock on day {}".format(dayPurchased))
                    print("Sold stock on day {}".format(j))

        # bottom right cell is the answer for upto k transactions on day len_stocks
        return arr[k][len_stocks - 1]