# https://leetcode.com/problems/combination-sum-ii
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
            
        def helper(combo, idx):
            if sum(combo) > target:
                return
            
            if sum(combo) == target:
                res.add(tuple(sorted(combo)))
                return
            
            for i in range(len(candidates)):
                # we track duplicates in candidates by tracking their index in a dict
                if i not in idx:
                    combo.append(candidates[i])
                    # note that you are tracking an element at i, value doesn't matter
                    idx[i] = None
                    
                    helper(combo, idx)
                    
                    # backtrack
                    combo.pop()
                    # delete i key from idx
                    del idx[i]

        helper([], dict())
        return [list(i) for i in res]