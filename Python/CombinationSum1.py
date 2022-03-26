# https://leetcode.com/problems/combination-sum/submissions/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        
        def helper(combo, sumCombo):
            if sumCombo > target:
                return
            
            if sumCombo == target:
                # we're adding sorted tuple to avoid duplicates
                # else we will add [2,3,3], [3,3,2] etc.
                res.add(tuple(sorted(combo)))
                # cant add more since all nums are positive
                # so we'll always overshoot target after this stage
                return
            
            # sum of combo is less than target
            for i in candidates:
                combo.append(i)
                helper(combo, sumCombo + i)
                combo.pop()
            
        
        helper([], 0)
        return [list(i) for i in res]
        