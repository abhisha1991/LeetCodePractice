# https://www.youtube.com/watch?v=oDhu5uGq_ic
def buy_sell(k, stocks):
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

print(buy_sell(3, [2, 5, 7, 1, 4, 3, 1, 3]))
print(buy_sell(3, [1, 1, 1, 1, 1, 1, 1, 1]))
print(buy_sell(3, [1, 2, 3, 4, 5, 6]))
print(buy_sell(3, list(reversed([1, 2, 3, 4, 5, 6]))))