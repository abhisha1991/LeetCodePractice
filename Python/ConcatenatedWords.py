# https://leetcode.com/problems/concatenated-words
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set()
        for w in words:
            wordset.add(w)
        
        res = []
        # can add a cache to in this function to check: word in cache, then return true early on (optimization)
        def dfs(word):
            for i in range(1, len(word)):
                left = word[:i]
                right = word[i:]
                # check if left and right are in wordset
                # if not, check which one is and do a dfs for the other
                if left in wordset and right in wordset:
                    return True
                elif left in wordset and dfs(right):
                    return True
                elif right in wordset and dfs(left):
                    return True
                
            return False
        
        for w in words:
            if dfs(w):
                res.append(w)
            
        return res