# https://leetcode.com/problems/coin-change/
# https://www.youtube.com/watch?v=PafJOaMzstY&t=382s
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        lencoin = len(coins)
        arr = []
        
        for c in range(lencoin):
            # create an array of dims rows = number of coins, cols = size of amount (starting 0 index)
            # add row by row
            arr.append([sys.maxsize] * (amount+1))
            # amt is current amount
            # note we want to go to amount+1, because we want to include a col for final amount 
            for amt in range(amount + 1):
                # if amount is 0, then no coins are needed
                if amt == 0:
                    arr[c][amt] = 0
                    continue
                
                # we can only add our current coin if its less than the amount, else leave as maxsize
                # notice c == 0 is handled as a special case because there is no coin "above" it in arr, ie, c=-1
                if c == 0 and coins[c] <= amt:
                    arr[c][amt] = 1 + arr[c][amt - coins[c]] 
                    continue
                    
                # either we can use 1 coin of current value or not
                # if we don't use current coin, just return whatever was above in arr, ie, arr[c-1][amt]
                # if we do use current coin, return 1 + arr[c][amt - coins[c]]
                
                useCoin = sys.maxsize
                dontUseCoin = arr[c-1][amt]
                
                if coins[c] <= amt:
                    useCoin = 1 + arr[c][amt - coins[c]]
                
                arr[c][amt] = min(dontUseCoin, useCoin)
        
        # this >= condition below is important, because we can have numbers greater than sys.maxsize
        # consider coins = [2] and amount = 3
        if arr[c][amount] >= sys.maxsize:
            return -1
        
        return arr[c][amount]