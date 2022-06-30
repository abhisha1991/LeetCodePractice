# https://leetcode.com/problems/custom-sort-string/
from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic = defaultdict(int)
        # create a freq counter for all letters in 's'
        for i in s:
            dic[i] +=1
        
        res = []
        # go through order
        for o in order:
            # if char exists in 's'
            if o in dic:
                # then add all those chars x freq in res
                res.extend([o] * dic[o])
                # delete that key from counter dictionary since we have handled that character
                del dic[o]

        # for the remaining chars that were not handled
        # append them to the end. For each char, add freq number of additions to the end of res
        for k,v in dic.items():
            res.extend([k] * v)
            
        return ''.join(res)res
        
        
        