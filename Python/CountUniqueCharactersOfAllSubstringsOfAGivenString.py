# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string
# https://www.youtube.com/watch?v=eN8zATT702M
from collections import defaultdict
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        letterMap = defaultdict(list)
        
        for i in range(len(s)):
            letterMap[s[i]].append(i)
        
        total = 0
        for k in letterMap.keys():
            indexes = letterMap[k]  
            for i in range(len(indexes)):
                left = None
                right = None
                
                # calculate left
                if i != 0:
                    # L X X L X X X 
                    # for 2nd L 
                    left = indexes[i] - indexes[i-1]
                else:
                    # X X L X X
                    # for the L above
                    left = indexes[i] + 1
                
                # calculate right
                if i == len(indexes)-1:
                    # L X X L X X X
                    # 2nd L calculation
                    right = len(s) - indexes[i]
                else:
                    # L X X L X X X
                    # first L calculation
                    right = indexes[i+1] - indexes[i]
                
                # left * right is the total number of ways you can have brackets on each side of a char
                # such that the char is unique in that substring formed between the brackets
                # consider X X L X X X L
                # for the first L, on the LEFT, we can have ( X X L X X X ) as one substring where L is unique
                # we can also have X ( X L X X X ), as a substring where L is unique
                # finally, we can have X X ( L X X X ) as a substring where L is unique
                # for the first L, on the RIGHT, we can have ( X X L X X X ), ( X X L X X ) X, ( X X L X) X X and 
                # finally, ( X X L) X X X
                # so total number of substrings is left x right = 3 x 4 = 12
                total += left * right
        
        return total