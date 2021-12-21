# Variant of buy sell stock
# section 5.7 from EPI
# second buy sell can only happen after the first transaction
import sys
def buyselltwice(arr):
    if len(arr) == 0:
        return None
    
    mini = arr[0]
    profit = 0
    fwd = [0] * len(arr)
    for i in range(1, len(arr)):
        if arr[i] < mini:
            mini = arr[i]
        
        if arr[i] - mini > profit:
            profit = arr[i] - mini
        # store all the forward profits in an array
        # fwd[i] is the max profit from 1 trasaction from elements 0:i
        fwd[i] = arr[i] - mini

    maxi = arr[-1]
    # iterate from the back to front
    for i in range(len(arr)-1, 1, -1):
        if arr[i] > maxi:
            maxi = arr[i]
        
        # this statement is imp
        # it says if the 2nd trasaction, 
        # ie, maxi - arr[i] added to the max profit up till i-1 elements, ie, fwd[i-1] is the largest
        # then that becomes total profit
        totalTempProfit = maxi - arr[i] + fwd[i-1]
        if totalTempProfit > profit:
            profit = totalTempProfit

    print("total profit is {}".format(profit))

buyselltwice([1,2,3,4,10])
buyselltwice([1,1,1,1,1])
buyselltwice([1,2,9,8,12,4,1,0])

    

 