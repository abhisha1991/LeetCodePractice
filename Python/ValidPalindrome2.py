# https://leetcode.com/problems/valid-palindrome-ii/submissions/
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        count = 0
        ls = len(s)
        i, j = 0, ls-1
        while i< ls/2:
            if s[i] != s[j]:
                return self.ispal(s, i+1,j) or self.ispal(s, i, j-1)
            i +=1
            j -=1
        return True
    
    def ispal(self, s, i, j):
        return s[i:j+1] == list(reversed(s[i:j+1]))   

    # this is the recursive solution
    # this is not accepted as it is exceeding time, need to investigate why
    # count stores number of violations where the first and last char were not equal
    # count starts with 0, is allowed to be maximum ==1
    def helper(self, s, count, ls):
        if count > 1:
            return False
        if ls <= 1:
            return True
        if s[0] != s[-1]:
            return self.helper(s[1:], count+1, ls-1) or \
        self.helper(s[:-1], count+1, ls-1)
        else:
            return self.helper(s[1:-1], count, ls-2)