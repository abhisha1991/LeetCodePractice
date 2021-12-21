# https://leetcode.com/problems/combination-sum-iii/submissions/
class Solution(object):
    def __init__(self):
        self.comb = []
        
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        arr = set()
        self.helper(k, n, arr)
        return self.comb
    
    def helper(self, k, n, arr):
        # sum cant be <0 and we need to stick to array length of k
        if n < 0 or len(arr) > k:
            return
        
        if len(arr) == k and n == 0 and list(arr) not in self.comb:
            # its important to add list(arr) and not arr. Why?
            # because list(arr) creates a new list, and just arr is a reference
            self.comb.append(list(arr))
            return
        
        for i in range(1,10):
            #  cant have duplicates
            if i not in arr:
                arr.add(i)
                self.helper(k, n-i, arr)
                # discard does not throw error if element is not found
                # remove does throw error if element is not found
                arr.discard(i)