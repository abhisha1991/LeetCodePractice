# https://leetcode.com/problems/find-and-replace-pattern/
# https://leetcode.com/problems/find-and-replace-pattern/discuss/167943/Easy-Python-Solution-using-dictionary
from collections import defaultdict

class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        plen = len(pattern)
        words = [x for x in words if len(x) == plen]
        res = []
        pset = set(pattern)
        psetlen = len(pset)
        
        for w in words:
            wset = set(w)
            wsetlen = len(wset)
            # set gets distinct elements, so we're comparing their lengths
            if psetlen == wsetlen:
                m1 = self.getMapping(w, pattern)
                m2 = self.getMapping(pattern, w)
                # the positions of the alphabets must also correspond
                if sorted(m1.values()) == sorted(m2.values()):
                    res.append(w)
        return res
        
        
    def getMapping(self, arr1, arr2):
        dic = defaultdict(list)
        for i in range(0, len(arr1)):
            dic[arr1[i]].append(i)
        return dic
        