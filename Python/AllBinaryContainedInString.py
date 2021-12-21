#https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/
class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        if N == 1:
            return str(N) in S.replace('0','')
        
        for i in range(1, N+1):
            # get binary rep of number
            x = format(i, "b")
            print ("x is " + x)
            if x not in S:
                return False
            
        return True