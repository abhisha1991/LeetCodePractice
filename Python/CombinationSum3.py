# https://leetcode.com/problems/combination-sum-iii/submissions/
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1,10)]
        res = set()
        
        def helper(combo):
            if sum(combo) > n or len(combo) > k:
                return
            
            if sum(combo) == n and len(combo) == k:
                # create a tuple of a sorted list of the combo (which is a set)
                # this is to avoid dupe entries in res
                res.add((tuple(sorted(list(combo)))))
                return
            
            for i in candidates:
                # cant have dupes in combo
                # if condition is needed, else we will go into infinite helper call
                if i not in combo:
                    combo.add(i)
                    helper(combo)
                    combo.remove(i)

        helper(set())
        return [list(i) for i in res]
        