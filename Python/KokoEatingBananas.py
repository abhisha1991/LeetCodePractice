# https://leetcode.com/problems/koko-eating-bananas/
class Solution:
    def __init__(self):
        self.k = None
    
    # accepted answer, time is o(len(piles) * log(max(piles)))
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        # binary search
        while l <= r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                # this is a better way to do the hours consumed calculation than in approach (minEatingSpeed1)
                hours += math.ceil(p/k)
            
            if hours <= h:
                res = min(res, k)
                r = k-1
            else:
                l = k+1
        return res
        
    # this is the right approach, but for some reason we get TLE on this input
    '''
    [312884470]
    312884469
    '''
    def minEatingSpeed1(self, piles: List[int], h: int) -> int:
        maxk = max(piles)
        arr = [i for i in range(1, maxk+1)]
        self.k = maxk
        
        def binsearch(low, high):
            if low > high:
                return
            
            mid = (low+high)//2
            res = self.canEatWithK(arr[mid], list(piles), h)
            if res and arr[mid] < self.k:
                self.k = arr[mid]
                # try and optimize and find lower k
                binsearch(low, mid-1)
                
            elif not res:
                # k was too small a rate, so increase by looking to the right of the array
                binsearch(mid+1, high)
        
        binsearch(0, len(arr)-1)
        return self.k
    
    def canEatWithK(self, k, p, remaining):
        # keep popping from p
        while p:
            first = p.pop(0)

            # this piece is saying that
            # say first = 11, and i = 3 (eating speed), then 11/3 = 3, so it means we will
            # take 3 hours to finish 9 bananas, then we're still left with 2 bananas (9+2=11)
            # so we need to add 1 to our hours consumed, that's what (if first > i) is doing

            # on the other hand, if first = 2 and i = 3 (eating speed), then 2/3=0
            # but we will actually need 1 hour to finish those 2 bananas, thus we take max of 1 and first/i
            consumed = max(1, int(first/k))
            if first > k:
                consumed +=1

            remaining -= consumed
            # we've run out of time but still have 1 or more piles left
            if remaining <= 0 and p:
                return False

        # we've finished all piles and still have time left
        if not p and remaining >= 0:
            return True
            
    # this gives TLE, this is the brute force way
    # time complexity is o(max(piles) * len(piles))
    def minEatingSpeed2(self, piles: List[int], h: int) -> int:
        maxk = max(piles)
        
        # start with 1 and move to maxk
        for i in range(1, maxk+1):
            # create a new list of piles so we don't modify the original
            p = list(piles)
            # set remaining time to be h
            remaining = h
            if self.canEatWithK(i, p, remaining):
                return i
        
        return maxk