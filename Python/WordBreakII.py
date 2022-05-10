# https://leetcode.com/problems/word-break-ii/
class Solution:
    def __init__(self):
        self.res = []
        
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if len(s) == 0:
            return []
        
        string = s
        
        def dfs(idx, path):
            if idx >= len(string):
                # remember that initially, we would have added an extra space before the 1st word
                # thus we do the stripping of spaces from the ends of the string
                self.res.append(path.strip(' '))
                return
            
            for w in wordDict:
                if string[idx:].startswith(w):
                    # keep adding word to path so far, remember to add space in between
                    dfs(idx + len(w), path + ' ' + w)
        
        
        dfs(0, '')
        return self.res