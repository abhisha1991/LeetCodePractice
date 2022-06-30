# https://leetcode.com/problems/valid-palindrome-iii/
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        
        visited = dict()
        def helper(string, i, j):
            # base case
            if i >= j:
                return 0
            
            # base case
            if i == j-1:
                return 1 if string[i] != string[j] else 0
            
            # if memoized
            if (i,j) in visited:
                return visited[(i,j)]
            
            # if the 2 chars are equal
            # then shrink on both sides, i+1, j-1 and call helper
            if string[i] == string[j]:
                visited[(i,j)] = helper(string, i + 1, j - 1)
            
            else:
                # if 2 chars are not equal
                # then we can shrink from either left or right
                # choose the minimum of the 2 
                # always remember to add 1 since there was a mismatch 
                # for the current comparison, ie, string[i] != string[j]
                visited[(i,j)] = 1 + min(helper(string, i+1, j), helper(string, i, j-1))
            
            return visited[(i,j)]
        
        n = len(s)
        helper(s, 0, n-1)
        if visited[(0, n-1)] <= k:
            return True
        return False