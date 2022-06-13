# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9 + 7
        '''
        say n = 3
        now we have p1, p2, p3 and d1, d2, d3
        now di must come after pi
        
        So lets place Pis in an unconstrained manner
        
        say p1, p2, p3
        
        try to place d3
        p1, p2, p3, {d3} --> 1 way only
        
        try to place d2
        p1, p2, {d2}, p3, {d3}  or  
        p1, p2, p3, {d2}, {d3}  or  
        p1, p2, p3, {d3}, {d2} --> 3 ways   
        
        try to place d1
        p1, {d1}, p2, {d2}, p3, {d3}  or
        p1, p2, {d1}, {d2}, p3, {d3}  or
        p1, p2, {d2}, {d1}, p3, {d3}  or
        p1, p2, {d2}, p3, {d1}, {d3}  or
        p1, p2, {d2}, p3, {d3}, {d1} --> 5 ways
        
        this was with 1 combo of p1, p2, p3 placement, that could have beeen also, p2, p3, p1 
        or in general, arranged in n! ways
        
        so there are 5 ways of delivery for each of the n! ways of pick up
        
        5 = 2 x 3 - 1 => 2n-1
        
        so the answer is n! * (2n-1)
        '''
        ans = 1
        for i in range(1, n+1):
            # this is the n factorial buildup
            ans = ans * i
            # this is to place the deliveries, 1, 3, 5, 7
            ans = ans * (2 * i - 1)
        
        
        return ans % mod