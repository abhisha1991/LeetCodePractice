# https://leetcode.com/problems/implement-strstr
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        if haystack == "":
            return -1
        
        if len(needle) > len(haystack):
            return -1
        
        if len(needle) == len(haystack):
            if needle == haystack:
                return 0
            return -1
        
        n = len(needle)
        # iterate through chunks of the haystack, 
        # which are of needle size and compare that part of the haystack with the needle
        for i in range(len(haystack)-n+1):
            compare = haystack[i:i+n]
            if compare == needle:
                return i
        
        return -1