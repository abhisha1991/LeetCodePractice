class Solution:
    def getFactors(self, n):
        if n == 1: return []
        res = []
        
        def dfs(path = [], rest = 2, target = n):
            if len(path) > 0:
                res.append(path + [target])
                
            for i in range(rest, int(math.sqrt(target)) + 1): # i <= target//i, i.e., i <= sqrt(target)
                if target % i == 0:
                    dfs(path + [i], i, target//i)
        
        dfs([], 2, n)
        return res

    # gets a TLE, but not sure I understand why
    def getFactors2(self, n: int) -> List[List[int]]:
        if n == 1:
            return []
        
        self.res = set()
        self.original = n
        
        def factors(n, start, arr):
            if n == 1:
                self.res.add(tuple(arr))
                return
            
            i = start
            while i <= n:
                # we don't want i to be the original number, say 10 was original
                # then if i were 10, then we would have to include a factor like 10 x 1, 
                # but 1 is not considered a factor according to the question, thus we ignore combos like 10x1, or 1x10
                if n % i != 0 or i == self.original:
                    i+=1
                    continue
                
                arr.append(i)
                # we have the start number in the params set to 'i', else we would have to do self.res.add(tuple(sorted(arr)))
                # instead of self.res.add(tuple(arr)) when inserting into res
                # why? our alternative is to start at number 2 everytime instead of 'i' when we call factor
                # as a result, if we were evaluating 10, we would get 2,5 and 5,2 if we always used 2 instead of 'i'
                # and thus we'd need to sort before insertion, so that we don't add both (2,5) and (5,2) as factors of 10
                factors(n//i, i, arr)
                
                arr.pop()
                i +=1
        
        factors(n, 2, [])
        return [list(x) for x in self.res]