# https://leetcode.com/problems/coin-change-2
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if len(coins) == 0:
            return 0
        
        if amount == 0:
            return 1
        
        lencoin = len(coins)
        arr = []
        
        for c in range(lencoin):
            # create an array of dims rows = number of coins, cols = size of amount (starting 0 index)
            # add row by row, currently there are 0 ways to make change for all amounts
            arr.append([0] * (amount+1))
            # amt is current amount
            # note we want to go to amount+1, because we want to include a col for final amount 
            for amt in range(amount + 1):
                # if amount is 0, then there's 1 way to make change - don't choose anything
                if amt == 0:
                    arr[c][amt] = 1
                    continue
                
                # if our current coin is larger than amount, so we cant even choose it
                # so we must rely on the only option we have, not choosing this coin
                if c >= 1 and coins[c] > amt:
                    arr[c][amt] = arr[c-1][amt]
                    continue
                
                # we can only add our current coin if its less than or equal to the amount
                # handle index 0 for coin in a special way, since we can't go to c-1 (needed to be done for general case)
                if c == 0 and coins[c] <= amt:
                    if amt % coins[c] == 0:
                        # there's only 1 way to reach say 4 amount with current coin '1' in list of coins [1,2,5]
                        # 1+1+1+1 = 4
                        arr[c][amt] = 1
                    else:
                        # there's 0 ways to reach say 4 amount with current coin '3' in list of coins [3,5]
                        # this is why we do the mod division check
                        arr[c][amt] = 0
                    continue
                    
                # either we can use 1 coin of current value or not
                # if we don't use current coin, total num ways = whatever was above in arr, ie, arr[c-1][amt]
                # if we do use current coin, total num ways = arr[c][amt - coins[c]]
                arr[c][amt] = arr[c][amt - coins[c]] + arr[c-1][amt]
        
        return arr[c][amount]