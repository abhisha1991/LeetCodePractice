# https://leetcode.com/problems/coin-change/
# https://www.youtube.com/watch?v=PafJOaMzstY&t=382s
import time
import sys

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        x = time.time()
        print(x)
        count = len(coins)
        arr = []

        for i in range(count):
            flag = True
            for j in range(0, amount + 1):
                if flag:
                    arr.append([sys.maxsize] * (amount + 1))
                    flag = False

                if j == 0:
                    arr[i][j] = 0
                    continue

                if i == 0:
                    if j < coins[i]:
                        continue
                    else:
                        arr[i][j] = 1 + arr[i][j - coins[i]]
                    continue

                if j < coins[i]:
                    arr[i][j] = arr[i - 1][j]
                else:
                    arr[i][j] = min([1 + arr[i][j - coins[i]], arr[i - 1][j]])

        y = time.time()
        print(y)
        print(y - x)
        if arr[count - 1][amount] >= sys.maxsize:
            return -1
        else:
            return arr[count - 1][amount]
