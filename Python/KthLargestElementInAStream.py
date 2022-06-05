# https://leetcode.com/problems/kth-largest-element-in-a-stream
from heapq import *
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        # keep the size of heap limited to k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # keep size of heap limited to k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        # element at top of minheap will be k largest, ie, the smallest of the top k largest elements
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)