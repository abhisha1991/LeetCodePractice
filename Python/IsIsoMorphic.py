# https://leetcode.com/problems/isomorphic-strings/
from collections import defaultdict


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slen = len(s)
        st_dict = defaultdict(list)
        for i in range(0, slen):
            st_dict[s[i]].append(t[i])

        all_values = []
        for k,v in st_dict.items():
            setv = set(v)
            for x in setv:
                if x in all_values:
                    return False
                else:
                    all_values.append(x)

            if len(setv) > 1:
                return False

        return True

s = Solution()
s.isIsomorphic("ab", "aa")
