# https://leetcode.com/problems/word-break/description/
class Solution:
    def __init__(self):
        self.res = False
        
    def wordBreak(self, s, wordDict):
        if len(s) is 0:
            return True
        
        string = s
        # dictionary contains key=idx in string where we have found a word in wordDict
        # value doesnt matter, but for storing something, value = word (from wordDict) starting at idx
        dic = dict()
        
        def dfs(idx):
            # we were able to reach the end of the word
            # while constantly getting hits for words from wordDict in the string
            if idx >= len(string):
                self.res = True
                return
            
            # memoization
            if idx in dic:
                return
                
            for w in wordDict:    
                # check the start of the remaining string, 
                # if it begins with one of the words in wordDict
                if string[idx:].startswith(w):
                    dic[idx] = w
                    
                    dfs(idx + len(w))
        
        dfs(0)
        return self.res