# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        ans = 0
        start = 0
        for i in range(len(s)):
            if s[i] in dict.keys() and start <= dict[s[i]]:
                start = dict[s[i]] + 1
            else:
                ans = max(ans, i - start + 1)
            dict[s[i]] = i
        return ans