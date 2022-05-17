# https://leetcode.com/problems/moving-average-from-data-stream
class MovingAverage:

    def __init__(self, size: int):
        self.k = size
        self.arr = []
        self.sumK = 0

    def next(self, val: int) -> float:
        self.arr.append(val)
        self.sumK += val
        
        n = len(self.arr)
        if n <= self.k:
            return self.sumK / n 
        
        # keep a cumulative sum, pop from the front (least recent element) and subtract from cumulative sum
        # that way we have most up to date sum available to us for last k elements in o(1) time
        self.sumK -= self.arr.pop(0)
        return self.sumK / self.k

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)