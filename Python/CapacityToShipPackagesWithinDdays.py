# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # for least capacity of ship, if we have a ship that is less than the max weight
        # then we won't be able to transfer the package with the max weight amongst weights
        l = max(weights) 
        # for max capacity of ship, 
        # we can potentially ship everything in 1 day if we had a ship with cap = sum(weights)
        r = sum(weights) 
        # we're trying to find min capacity of ship, so initialize it with max
        cap = sys.maxsize
        
        # binary search
        while l <= r:
            m = (l+r)//2 # mid capacity of ship (remember to do int)
            d = days
            w = 0
            # flag captures whether ship with capacity 'm' can transfer the packages in d days
            flag = False
            while d > 0: # while we have days available
                # totalw represents total weight carried on a SINGLE day
                # this can at max be the potential ship capacity 'm'
                totalw = 0
                # keep incrementing total weight we can carry till we reach 'm'
                while w < len(weights) and totalw < m:
                    totalw += weights[w]
                    w +=1
                
                # if we're in excess of m, reduce 'w' index by 1
                # since we're allowed to carry only <=m
                if totalw > m:
                    w -=1
                
                # reduce number of days since we were able to carry <=m weight for this day
                d -=1
                
                # if we have reached the end of our weights arr and we still have >=0 days left
                # then we were able to ship all packages in d days with 'm' capacity of the ship
                if d >=0 and w == len(weights):
                    flag = True
                    break
            
            # if we were able to ship with m capacity
            # update our answer and try and optimize by reducing our right part of the binary search
            if flag:
                cap = min(cap, m)
                r = m-1
            else:
                # we were unable to ship all packages with m capacity
                # so increase lower bound capacity to m+1 (ie, update left part of binary search)
                l = m+1
        
        return cap