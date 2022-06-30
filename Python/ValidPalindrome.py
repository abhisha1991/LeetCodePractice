# https://leetcode.com/problems/valid-palindrome/submissions/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = []
        for i in s:
            if (i >= '0' and i <= '9') or (i >= 'a' and i <= 'z'):
                res.append(i)
        
        return res == res[::-1]