# https://leetcode.com/problems/number-of-matching-subsequences
from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # group words by start letter so that they will appear together
        '''
        d --> [dog, dot, dorm]
        c --> [car, cat]
        '''
        group = defaultdict(list)
        res = 0
        for w in words:
            start = w[0]
            group[start].append(w)
        
        for i in range(len(s)):
            start = s[i]
            
            if start in group:
                remain = [x[1:] for x in group[start]]
                # delete original group from dictionary that starts with 'start'
                del group[start]
                
                # add new groups for each of the remaining words that are not empty
                for r in remain:
                    # if remaining word became empty, then add to res count
                    if r == '':
                        res +=1
                        continue
                        
                    first = r[0]
                    group[first].append(r)
                
        return res