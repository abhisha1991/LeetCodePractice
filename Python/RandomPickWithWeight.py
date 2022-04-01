# https://leetcode.com/problems/random-pick-with-weight
# https://www.youtube.com/watch?v=fWS0TCcr-lE
class Solution:

    def __init__(self, w: List[int]):
        self.cumSum = []
        self.total = 0
        # say you have an array, [1,5,2]
        # cum sum will be [1, 6, 8]
        
        for i in w:
            self.total +=i
            # essentially, we're creating buckets here which is proportional to the element size itself
            self.cumSum.append(self.total)
        
    
    def pickIndex(self) -> int:
        # pick a float between 0 and 1, inclusive
        x = random.uniform(0,1)
        # this target is the key concept
        # say you generate a random number above 0.6, thus target will be 0.6 * 8 = 4.8
        # now the idea is that we need to find a number in cumSum that is just above 4.8, so we find 6
        # and thus we return the idx corresponding to 6, which is 1
        # this can be done slowly, in linear search, but because we know cumSum is sorted, we can apply binary search here
        target = x * self.total
        
        low, high = 0, len(self.cumSum)
        while low < high:
            mid = int((low + high)/2)
            if target > self.cumSum[mid]:
                low = mid +1
            else:
                high = mid
                
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()