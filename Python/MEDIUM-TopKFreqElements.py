# https://leetcode.com/problems/top-k-frequent-elements/description/
from collections import defaultdict
import time


# Not optimal, but a pretty good solution
class Solution:
    def __init__(self):
        self.ans = []

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        self.top_k_util(nums, k)
        return self.ans

    def top_k_util(self, nums, k):
        # print("nums is", nums)
        # print("k is ", k)
        dic = defaultdict(int)
        maxk = 0
        maxv = 0
        for i in nums:
            dic[i] += 1
            if maxv < dic[i]:
                maxv = dic[i]
                maxk = i

        self.ans.append(maxk)
        nums = [x for x in nums if x != maxk]
        if k > 1:
            self.top_k_util(nums, k - 1)
        return

# Actual correct solution, pretty simple to follow
class Solution2:
    def __init__(self):
        self.ans = []

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # here dic just captures frequency of each element in the list
        # key = element in the list, value = its frequency in the list
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1

        # bucket essentially flips the equation
        # it stores frequency as key, and the element of the list as the value
        bucket = defaultdict(list)
        for x, v in dic.items():
            if len(bucket[v]) == 0:
                bucket[v] = [x]
            else:
                bucket[v].append(x)

        print("bucket", bucket)
        res = []
        while len(res) < k:
            # find the max frequency
            maxk = max(bucket)
            print("maxk", maxk)
            # add the element of the original list with max frequency to result
            res.extend(bucket[maxk])
            print("res", res)
            # delete the bucket entry with the highest frequency so you can pick the next highest frequency
            del bucket[maxk]

        return res[0:k]

s2 = Solution2()
s2.topKFrequent([1,1,1,2,2,3], 2)