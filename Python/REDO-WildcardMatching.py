# https://www.youtube.com/watch?v=3ZDZ-N0EPV0
# https://leetcode.com/problems/wildcard-matching/description/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        say string  = xaylmz
        say pattern = x?y*z
           ''   x   ?   y   *   z
       ''  T    F   F   F   F   F
        
        x  F    T   F   F   F   F
         
        a  F    F   T   F   F   F
        
        y  F    F   F   T   T   F
        
        l  F    F   F   F   T   F
        
        m  F    F   F   F   T   F
        
        z  F    F   F   F   T   T
        
        answer is at bottom right, res[m-1][n-1]
        
        1. if pattern[j] == string[i] or pattern[j] == '?' --> then look at diagonally top left
        
        2. if pattern[j] == '*' --> then look at res[i-1][j] or res[i][j-1], ie, left or top
            - left implies that * accounts for 0 char in string (example 'xay' vs 'x?y*')
            - top implies that * accounts for as 1 or more char in string (example 'xaylm' vs 'x?y*')
        
        3. if pattern[j] != string[i], then false
        
        res[0][0] is always true, since empty pattern matches empty string
        1st column is always false since empty pattern can never match a string of any length > 0
        1st row is mostly false, but can be true if pattern[0] == '*'
        '''
        m = len(s)
        n = len(p)
        
        if m == 0 and n == 0:
            return True
        
        # string is non empty but pattern is empty
        if n == 0:
            return False
        
        res = [[False] * (n+1) for i in range(m+1)]
        res[0][0] = True
        
        # 1st col is always false
        for i in range(1, m+1):
            res[i][0] = False
        
        # if pattern starts with *, then we have 1st row be true
        # till this is the case
        if p[0] == '*':
            for i in range(1, n+1):
                if p[i-1] == '*':
                    res[0][i] = True
                else:
                    # p[i-1] is not * anymore, so break!
                    # will handle a case like *ab* -- the 2nd * should NOT be true!
                    break
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    # we have already taken care of 1st row and 1st col
                    continue
                
                # now i,j are at least 1 each
                # ii and jj are pointing to string and pattern indices respectively
                # why -1? because we have an extra space in front of both pattern and string, which 
                # makes res dimensions 1 bigger than pattern/string
                ii = i-1
                jj = j-1
                
                if p[jj] == s[ii] or p[jj] == '?':
                    res[i][j] = res[i-1][j-1]
                    continue
                
                if p[jj] == '*':
                    res[i][j] = res[i-1][j] or res[i][j-1]
                    continue
                
                # default is false when pattern[jj] != string[ii]
                    
        return res[m][n]