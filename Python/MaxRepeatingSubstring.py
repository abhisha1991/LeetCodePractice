# https://leetcode.com/problems/maximum-repeating-substring
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0
        
        res = 0
        # start with word
        s = word
        # see if s is in sequence
        while s in sequence:
            res += 1
            # if 1 'word' is there
            # expand s by concating 'word' to s
            # and try to find updated s (2 words back to back) again in sequence
            s += word
            
        return res
        