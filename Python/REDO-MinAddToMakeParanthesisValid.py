# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution(object):        
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        
        openbal = closebal = 0
        # open balance is used to keep track of the open brackets (excess open paranthesis)
        # close balance is used to keep track of the closed brackets (excess close paranthesis)
        # we cap open balance to reach -1, if it does, we know there are excess closed brackets, but we need a way to track this, ie use closebal
        # if there are excess closed brackets (ie, openbal is -1), we make open balance as 0 and we add to the close balance (ie, we ack that there is an extra closed bracket) 
        for s in S:
            if s == "(":
                openbal +=1
            else:
                openbal +=-1
            if openbal == -1:
                closebal +=1
                openbal +=1

        return openbal + closebal