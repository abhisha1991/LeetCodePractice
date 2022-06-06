# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        consider example, [1,7,11] and [2,4,6] and k = 5
        below are the pairs that can be formed    
        
            2      4     6
        
        1  (1,2)  (1,4)  (1,6)
        
        7  (7,2)  (7,4)  (7,6)
        
        11 (11,2) (11,4) (11,6)
        
        what we do is we initialize the heap with the first column of the above pairs
        heap format: [sum, n1, n2, idx of n2]
        
        heap = [(3, 1, 2, 0), (9, 7, 2, 0), (13, 11, 2, 0)]
                          |
                          |---> this last element is going to be the idx of nums2 element
                           
        the 0 represents the index of element '2' in nums2
        
        now we pop from heap and add it to our solution, since it will be the smallest sum always
        (given that both nums1 and num2 are sorted and we're taking both their first elements)
        ans = [[1,2]]
        
        when popping from heap, we use the index we referred to for element '2', ie, 0 
        and we insert the next element into the heap using this index
        
        in effect, we increment 0 by 1 and are effectively looking up 2nd element of nums2, ie, 
        pair = (1,4) to insert into the heap, so now heap becomes
        
        heap = [(5, 1, 4, 1), (9, 7, 2, 0), (13, 11, 2, 0)]
                          |
                          |---> this last element is going to be the idx of nums2 element, ie, 4
        
        we pop from the heap again and push into ans, we get ans = [[1,2], [1,4]]
        
        when popping from heap, we take index of element '4' in nums2 and increment by 1
        and we insert pair = (1,6) into heap, so heap is:
        
        heap = [(7, 1, 6, 2), (9, 7, 2, 0), (13, 11, 2, 0)]
        
        and we continue on like this till we have either exhausted the heap or reached our k elements 
        '''
        ans = []
        pq = []
        heapq.heapify(pq)
        lenNums2 = len(nums2)
        
        if not nums1 or not nums2:
            return []
        
        # initialize heap
        for n1 in nums1:
            n2 = nums2[0]
            heapq.heappush(pq, (n1 + n2, n1, n2, 0))
        
        while pq and k > 0:
            summ, n1, n2, n2Idx = heapq.heappop(pq)
            ans.append([n1, n2])
            k -=1
            if n2Idx == lenNums2-1:
                continue
            
            n2Idx +=1
            n2 = nums2[n2Idx]
            heapq.heappush(pq, (n1 + n2, n1, n2, n2Idx))
        
        return ans

    # gives memory limit exceeded
    # time wise this will be k^2 log k in time complexity, if k < nums1.length and k < nums2.length
    def kSmallestPairs2(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # this n1, n2 is the key observation here
        # k is max 10^4, whereas nums1 and nums2 can be 10^5 in length
        # so we take the minimum of the 2 to find the top k items
        n1 = min(len(nums1), k)
        n2 = min(len(nums2), k)
        pairs = []
        
        for i in range(n1):
            for j in range(n2):
                pairs.append([nums1[i], nums2[j]])
        
        # sort by sum of nums1 item and nums2 item
        pairs = sorted(pairs, key=lambda x: x[0] + x[1])
        # return top k items
        return pairs[:k]
    
    # gives memory limit exceeded
    def kSmallestPairs3(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1 = len(nums1)
        n2 = len(nums2)
        pairs = []
        pq = []
        heapq.heapify(pq)
        
        for i in range(n1):
            for j in range(n2):
                # do -1 times the sum because we can only have min heaps in python
                # thus we want max sum elements to remain at the top, so they can be popped from heap
                pairs.append((-1 * (nums1[i] + nums2[j]), nums1[i], nums2[j]))
        
        for p in pairs:
            # push all items in pairs one by one
            heapq.heappush(pq, p)
            # limit size of heap to k, this ensures that we're popping out the largest items
            # and keeping only the k smallest items
            if len(pq) > k:
                heapq.heappop(pq)
        
        res = []
        for item in pq:
            # store only the elements, and not their sum in res
            res.append([item[1], item[2]])
        return res