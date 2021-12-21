# https://leetcode.com/problems/combination-sum/submissions/
class Solution(object):
    def __init__(self):
        self.comb = []
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.helper(candidates, target, [])
        return self.comb
    
    def helper(self, candidates, target, arr):
        if target < 0:
            return
            
        # target being 0 means that the sum is 0, ie, we have found a combination
        if target == 0:
            # this is to handle the duplicate case, that is why we sort array
            a = sorted(list(arr)) 
            if a not in self.comb:
                self.comb.append(a)
            return
        
        for c in candidates:
            arr.append(c)
            self.helper(candidates, target - c, arr)
            arr.remove(c)
        