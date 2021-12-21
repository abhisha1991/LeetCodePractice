# check if binary representation of a number has alternate 0s and 1s
# for example, 5 is 101 so return true
# for example, 7 is 111, so return false
# https://leetcode.com/problems/binary-number-with-alternating-bits/submissions/
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nstr = str(bin(n)[2:])
        if len(nstr) < 2:
            return True
        
        i = nstr[0]
        j = 1
        while j < len(nstr):
            if i == nstr[j]:
                return False
            i = nstr[j]
            j +=1
        return True