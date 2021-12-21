#https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        from collections import Counter
        dic = Counter(A)
        for key in dic:
            if dic[key]>1:
                return key
