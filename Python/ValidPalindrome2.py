# https://leetcode.com/problems/valid-palindrome-ii
class Solution:
    # O(n2) solution
    def validPalindrome_inefficient(self, s: str) -> bool:
        if self.isPalindrome(s, 0, len(s)):
            return True
        
        for i in range(len(s)):
            new_s = s[0:i] + s[i+1:]
            if self.isPalindrome(str(new_s), 0, len(new_s)):
                return True
        return False
     
    # this is O(n) solution
    def validPalindrome(self, s: str) -> bool:
        # does 2 passes over string, one allowing mismatch to be overlooked from left side
        # and the other allowing mismatch to be overlooked from right side

        # 2 pointers, start from begin and end, meet at middle
        i = 0
        j = len(s) - 1
        mismatch = 0
        
        # FIRST PASS
        while i <= j:
            if s[i] != s[j]:
                # allow mismatch to be overlooked from left side
                i +=1
                mismatch +=1
            else:
                i +=1
                j -=1
        
        # up to one mismatch allowed
        if mismatch <=1:
            return True
        
        # reset for 2nd pass
        i = 0
        j = len(s) - 1
        mismatch = 0
        
        # SECOND PASS
        while i <= j:
            if s[i] != s[j]:
                # allow mismatch to be overlooked from right side
                j -=1
                mismatch +=1
            else:
                i +=1
                j -=1
        
        # up to one mismatch allowed
        if mismatch <=1:
            return True
        
        return False
    
    def isPalindrome(self, s, i, j):
        return s[i:j+1] == s[i:j+1][::-1]