# https://leetcode.com/problems/the-kth-factor-of-n/
import math
import heapq
class Solution:
    # this is o(n)
    def kthFactor2(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, n+1):
            if n % i == 0:
                factors.append(i)
        
        if len(factors) >= k:
            return factors[k-1]
        return -1
    
    # the time complexity is o(sqrt(N) x logk)
    # sqrt(N) comes because we have to run through this loop sqrt(N) number of times
    # for each run in the loop, we need to insert into heap, which is a log(k) operation since heap size is <=k always
    def kthFactor(self, n: int, k: int) -> int:
        root = int(math.sqrt(n))
        # we need a max heap, python only has minheaps
        # so we need to insert negative values for max heap
        
        h = []
        heapq.heapify(h)
        
        # limit size of heap to k
        # this will ensure that the kth highest factor is always retained on top, which is what we want
        def heappushK(num):
            heapq.heappush(h, -num)
            if len(h) > k:
                heapq.heappop(h)
        
        for i in range(1, root+1):
            if n % i == 0:
                heappushK(i)
                # we're also adding the corresponding other factor into the heap
                # say we're seeing if 6 is divisible by 2, it is, so we add 2 to the heap
                # we also add 6/2 = 3 to the heap
                
                # check for this condition so that we don't add number twice, imagine factor=2, num=4
                # so we dont want to add 2 and 4/2=2 twice!
                if i != int(n / i): 
                    heappushK(int(n/i))
        
        if len(h) == k:
            return -heapq.heappop(h)
        
        return -1