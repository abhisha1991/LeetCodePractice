# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
        startWords = [''.join(sorted(s)) for s in startWords]
        startSet = set(startWords)
        
        res = 0
        for t in targetWords:
            for i in range(len(t)):
                # remove 1 char from target word at each position, sort it and compare against start words
                # why go the opposite route? because removing 1 char from target is much more scoped than
                # trying to add each of 26 chars to the end of each start word
                newt = t[:i] + t[i+1:]
                newt = ''.join(sorted(newt))
                if newt in startSet:
                    res +=1
                    break
        
        return res