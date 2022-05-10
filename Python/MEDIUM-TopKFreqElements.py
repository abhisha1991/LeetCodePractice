# https://leetcode.com/problems/top-k-frequent-elements/description/
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        dic = dict()
        revDic = defaultdict(list)
        h = []
        heapq.heapify(h)
        
        # create a frequency counter for the with nums[i] as keys
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] +=1
        
        # create a reverse dictionary with key = frequency,
        # value is going to be the nums[i] that had that frequency
        for key, val in dic.items():
            revDic[val].append(key)
        
        # insert the frequencies into a max heap
        for v in revDic.keys():
            heapq.heappush(h, -v)
        
        # till the size of result is k, keep taking max frequency out of heap
        # and keep adding to res the nums[i] that have this highest frequency
        while len(res) < k:
            v = -1 * heapq.heappop(h)
            vals = revDic[v]
            res.extend(vals)
        
        # return top k elements
        return res[:k]