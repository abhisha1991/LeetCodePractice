# https://leetcode.com/problems/palindromic-substrings/submissions/
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0
        # intialize matrix with all false
        mat = [[False] * n for i in range(n)]
        for i in range(n):
            # a single char is a substring and always a palindrome
            mat[i][i] = True
            count +=1
        
        l = 1
        # consider 1 length substring, then 2 length substring, then 3 length substring and so on
        while l < n:
            for i in range(n-l):
                j = i + l
                # j is end index so range will be n-l for i (else index j is out of bounds)
                if s[i] == s[j]:
                    if i+1 > j-1:
                        # if our string has crossed over, start index is more than end index
                        # then we are a palindrome, because so far we have met the condition of a palindrome
                        mat[i][j] = True
                    else:
                        mat[i][j] = mat[i+1][j-1]
                    # if its a palindrome from i to j, increase count
                    if mat[i][j]:
                        count +=1
            l +=1
        
        return count