'''
An investor has saved some money and wants to invest in the stock market. 
There are a number of stocks to choose from, and they want to buy at most 1 share in any company. 
The total invested cannot exceed the funds available. 
A friend who is a stock market expert has predicted the value of each stock after 1 year. 
Determine the maximum profit that can be earned at the end of the year assuming the predictions come true.

Example
saving = 250
currentValue = [175, 133, 109, 201, 97]
futureValue = [200, 125, 128, 228, 133]

To maximize profits, the investor should buy stocks at indices 2 and 4 for an investment of 109 + 97 = 206. 
At the end of the year the stocks are sold for 128+133 = 261, so total profit is 261-206 = 55

Example
saving = 30
currentValue = [1,2,4,6]
futureValue = [5,3,5,6]

Output = 6

Example
*saving = 500
currentValue = [150, 199, 200, 168, 153]
futureValue = [140, 175, 199, 121, 111]

Output = 0 since all of the stocks lost money*
'''
class Solution():
    def __init__(self, current, future, saving):
        self.cur = current
        self.future = future
        self.saving = saving
        assert(len(current) == len(future))
        
    def getMaxProfit(self):
        profit = 0
        arr = [(self.future[i], self.cur[i]) for i in range(len(self.cur))]

        # similar to knapsack problem, sort by sell value / buy value
        # ie, which gives us most profit, and then make those trades
        # assumes buy price is positive and not 0
        arr = sorted(arr, key=lambda x: x[0]/x[1], reverse=True)
        i = 0
        while self.saving >= 0 and i < len(arr):
            sell = arr[i][0]
            buy = arr[i][1]

            # if we cannot afford to buy, then move to next stock
            if self.saving - buy < 0:
                i +=1
                continue

            p = sell - buy 

            # we rather not buy and trade, if our profit is negative
            if p < 0:
                i +=1
                continue

            profit += p
            self.saving -= buy
            print(f"bought at {buy} and sold at {sell}, making profit: {p}, saving left: {self.saving}")
            i +=1

        if profit < 0:
            return 0
        return profit

s = Solution([175, 133, 109, 201, 97], [200, 125, 128, 228, 133], 250)
print(s.getMaxProfit())

s = Solution([1,2,4,6], [5,3,5,6], 30)
print(s.getMaxProfit())

s = Solution([150, 199, 200, 168, 153], [140, 175, 199, 121, 111], 500)
print(s.getMaxProfit())

s = Solution([100, 200, 300], [10, 400, 900], 5000)
print(s.getMaxProfit())

s = Solution([10000, 200, 300], [100000, 400, 10], 5000)
print(s.getMaxProfit())