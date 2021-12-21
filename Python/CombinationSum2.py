# https://leetcode.com/problems/combination-sum-ii
class Solution(object):
    def __init__(self):
        self.comb = []
        
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.helper(candidates, target, [], 0)
        return self.comb
    
    def helper(self, candidates, target, arr, start):
        if target < 0:
            return
        
        if target == 0:
            a = list(arr)
            a.sort()
            if a not in self.comb:
                self.comb.append(a)
            return
        
        for i in range(start, len(candidates)):
            arr.append(candidates[i])
            self.helper(candidates, target - candidates[i], arr, i+1)
            arr.remove(candidates[i])