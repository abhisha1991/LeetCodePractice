class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(a, b):
            n = len(a)
            count = 0

            # if there's more than 2 mismatches, then strings are not similar
            # since you're only allowed to swap 2 chars
            for i in range(n):
                if a[i] != b[i]:
                    count +=1
                if count > 2:
                    return False
            return True
        
        res = 0
        visited = set()
        
        if len(strs) == 0:
            return res
    
        def dfs(cur):
            if cur in visited:
                return
            
            visited.add(cur)
            for s in strs:
                if isSimilar(cur, s):
                    dfs(s)
        
        # we need a for loop at the outer most level because there may be disconnected components
        # and we want to go through all disconnected components
        # example [rats, star, arts,  tars] --> will have 2 groups - [star] and [rats, arts,  tars]
        # so if we start with 'rats' --> we'll be able to reach 'arts' and 'tars', but we won't reach star
        for s in strs:
            if s not in visited:
                dfs(s)
                res +=1
        
        return res