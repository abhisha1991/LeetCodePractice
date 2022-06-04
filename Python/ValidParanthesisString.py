# https://leetcode.com/problems/valid-parenthesis-string/
class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        
        if s[0] == ')':
            return False
        
        # stack tracks open bracket indexes
        stack = []
        # stars tracks indexes of star characters
        stars = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            
            elif s[i] == '*':
                stars.append(i)
            
            # we dont have anything to balance the close brackets with
            elif not stars and not stack and s[i] == ')':
                return False
            
            # prefer balancing a closed bracket, ie, s[i] with open bracket, rather than a star
            elif stack and s[i] == ')':
                stack.pop()
            
            # use start when open bracket stack is exhausted
            elif stars and not stack and s[i] == ')':
                stars.pop()
        
        # below condition is checking that the open brackets were balanced by the close brackets
        # we can make all star values to be empty strings, and have a valid string
        if not stack:
            return True
        
        # reaching here means we have open brackets left in excess, but closed brackets were solved
        # so we need the remaining stars to act as close brackets
        
        # if the remaining stars are less than open bracket demand, then we can't fulfill, so return false
        if len(stars) < len(stack):
            return False
        
        # insertion into stack and stars was done in increasing order, ie, the indices in these lists should be sorted
        while stack:
            # we are out of stars to balance the open brackets
            if not stars:
                return False
            
            # get the first index of open bracket
            openIdx = stack.pop(0)
            starIdx = None
            while stars:
                # if starIdx is less than open bracket idx, that's not useful for us
                # since we need the star to come after open bracket (so star can act as a closing bracket)
                # thus we need to keep popping, unitil we hit that condition
                starIdx = stars.pop(0)
                if starIdx > openIdx:
                    break
            
            if not starIdx or starIdx < openIdx:
                return False
            
            # balance out starIdx with openIdx, treating startIdx char as a closing bracket
            assert(starIdx > openIdx)
        
        # if there are still unbalanced open brackets
        # we were unsusccessful at using the stars for balancing
        return False if stack else True