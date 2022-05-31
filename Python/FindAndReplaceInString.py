# https://leetcode.com/problems/find-and-replace-in-string
from collections import defaultdict
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        res = ''
        lookup = defaultdict(list)
        for i in range(len(indices)):
            idx = indices[i]
            lookup[idx] = [sources[i], targets[i]]
        
        i = 0
        while i < len(s):
            # if index is in lookup and the word contains the source string
            if i in lookup and s[i:].startswith(lookup[i][0]):
                res += lookup[i][1] # add target
                i += len(lookup[i][0]) # increase i by the source that just matched
            else:
                res += s[i]
                i +=1
        return res