# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/
from heapq import *
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        pairs = []
        pq = []
        heapq.heapify(pq)
        
        for i in range(n1):
            for j in range(n2):
                # do -1 times the prod because we can only have min heaps in python
                # thus we want max prod elements to remain at the top, so they can be popped from heap
                pairs.append((-1 * (nums1[i] * nums2[j]), nums1[i], nums2[j]))
        
        for p in pairs:
            # push all items in pairs one by one
            heapq.heappush(pq, p)
            # limit size of heap to k, this ensures that we're popping out the largest items
            # and keeping only the k smallest items
            if len(pq) > k:
                heapq.heappop(pq)
        
        # the top element of the heap will be the answer, note we're accessing idx 0
        # which is the negative of the product, so we need to return -1 times that value
        return -pq[0][0]