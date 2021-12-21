# https://leetcode.com/problems/group-anagrams/description/
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        dic = defaultdict(list)
        for i in strs:
            key = i
            key = str(sorted(key))
            if key not in dic.keys():
                dic[key] = []
                dic[key].append(i)
            else:
                dic[key].append(i)
        for k,v in dic.items():
            res.append(v)
        return res