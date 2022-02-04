# https://leetcode.com/problems/valid-palindrome/submissions/
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = s.replace(' ', '')
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        
        return s == s[::-1]