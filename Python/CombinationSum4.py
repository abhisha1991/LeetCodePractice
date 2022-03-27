# https://leetcode.com/problems/combination-sum-iv/
# very similar to combination sum 1,2,3
# need to find an optimal way to handle these
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = set()
        
        def helper(combo):
            if sum(combo) > target:
                return
            
            if sum(combo) == target:
                res.add(tuple(combo))
                return
            
            for i in nums:
                combo.append(i)
                helper(combo)
                combo.pop()
        
        helper([])
        return len(res)