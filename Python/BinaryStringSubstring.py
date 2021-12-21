
# not optimal solution
# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/ 
# need to understand this well

class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        for i in range(1, N+1):
            if self.binary(i) not in S:
                return False
        
        return True
    
    def binary(self, i):
        return "{0:b}".format(i)