class Solution:
    # the same exact problem as word break
    # same exact method as here: https://www.youtube.com/watch?v=YcJTyrG3bZs
    def numDecodings(self, s: str) -> int:
        dic = dict()
        # create the mapping such that dic['1'] = 'A', dic['2'] = 'B' etc.
        for i in range(0, 26):
            j = ord('A') + i
            c = chr(j)
            dic[str(i+1)] = c
        
        string = s
        cache = dict()
        
        def dfs(idx):
            if idx >= len(string):
                return 1
            
            if idx in cache:
                return cache[idx]
            
            r = 0
            for w in dic:
                if string[idx:].startswith(w):
        
                    r += dfs(idx + len(w))
            
            cache[idx] = r
            return r
        
        dfs(0)
        # how many total ways are there to decode at index 0 is given at cache[0]
        return cache[0]