# https://leetcode.com/problems/stock-price-fluctuation/
import heapq
class StockPrice:
    def __init__(self):
        self.ts2price = dict()
        self.latestTs = 0
        # heaps mx and mn can store prices that are stale for a given ts, during minimum() and maximum() calls
        # we will attempt to keep popping from the heaps so we get rid off the stale prices for a given timestamp
        self.mx = []
        self.mn = []
        
        heapq.heapify(self.mx)
        heapq.heapify(self.mn)

    def update(self, timestamp: int, price: int) -> None:
        self.latestTs = max(self.latestTs, timestamp)
        self.ts2price[timestamp] = price
        heapq.heappush(self.mn, (price, timestamp))
        heapq.heappush(self.mx, (-price, timestamp))
        
    def current(self) -> int:
        return self.ts2price[self.latestTs]

    def maximum(self) -> int:
        # remember currp is going to be negative because its a max heap in python
        currp, ts = heapq.heappop(self.mx)
        
        while self.mx and -currp != self.ts2price[ts]:
            currp, ts = heapq.heappop(self.mx)
        
        # currp is negative, so push negative value itself to max heap as we were doing in update() line 19
        heapq.heappush(self.mx, (currp, ts))
        # return positive value, ie, -currp
        return -1 * currp

    def minimum(self) -> int:
        # we have the smallest price from the heap upon popping
        # we cannot return this currp because it may not be the "latest price corresponding to the ts"
        # we need to ultimately return a min price that is also "current"!
        # example input (ts, price): [[1, 50], [2, 20], [1, 30], [1,60]]
        '''
        ts2price looks like:
        1 --> 60
        2 --> 20
        
        if we draw the min heap for the above as (price, ts) we get
        
        
                            (20,2)
                            /     \
                        (50,1)    (30,1)
                        /
                     (60,1)   
        
        now if we want minimum, in the first shot itself, 
        we will check that ts2price[2] = 20 and this matches top of heap, so we can return 20 and pop 20
        
        after this, heap looks like
                              (30, 1)
                             /       \
                          (50,1)     (60,1)
        
        now if we want minimum, and we check top of heap, we see 30, but ts2price[1] = 60 not 30
        so 30 is a stale price, so we pop 30, now heap becomes
                                (50, 1)
                                /
                            (60,1)
        
        we check top of heap, we see 50, but ts2price[1] = 60 not 50, so 50 is a stale price, so we pop 50
        now heap is just (60,1). At this point ts2price[1] == top of heap, 
        ie, latest price at ts=1 == heap top
        
        so we return minimum price as 60
        '''
        currp, ts = heapq.heappop(self.mn)
        
        # below we are saying
        # keep popping from minheap to get potential min prices
        # if the min price we obtain ALSO happens to be the latest price - 
        # since ts2price always stores latest prices for a given ts - then break
        while self.mn and currp != self.ts2price[ts]:
            currp, ts = heapq.heappop(self.mn)
        
        # now we have a ts, currp pair which is minimum and reflects the latest price at time ts
        # so insert back into heap
        heapq.heappush(self.mn, (currp, ts))
        return currp


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()