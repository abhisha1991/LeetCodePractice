# https://leetcode.com/problems/valid-word-abbreviation/
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if '0' in abbr:
            idx = abbr.index('0')
            # if char 0 was at the start of abbr
            # or if we have something like s019b -- this is also not allowed since 0 cant be leading char
            if idx == 0 or not abbr[idx-1].isdigit():
                return False
        
        w = len(word)
        n = len(abbr)
        # i tracks word, j tracks abbr
        i = 0
        j = 0
        
        while i < w and j < n:
            if word[i] == abbr[j]:
                i +=1
                j +=1
                
            elif abbr[j].isdigit():
                k = j
                
                # parse the entire digit(s)
                # example, if the abbr was a10p -- then we'd need to parse 10 completely
                d = ''
                while k < len(abbr) and abbr[k].isdigit():
                    d += abbr[k]
                    k +=1
                    
                # increment i by d because we are skipping over all characters that are masked by its digit representation
                i += int(d)
                # k was the end of the digit positions
                # k is actually now pointing to the pos right after the last digit, in a10p, it is pointing to pos 3, ie, p
                j = k
                
            elif word[i] != abbr[j]:
                return False
        
        # if both indices were able to reach to the end
        return i == w and j == n 