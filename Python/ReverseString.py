# https://leetcode.com/problems/reverse-string-ii/
class Solution(object):
    def __init__(self):
        self.input = None
    
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i = 0
        j = k - 1
        self.input = list(s)
        slen = len(s)
        
        while i < slen:
            if j >= slen:
                self.helper(i, slen-1)
                i += 2*k
                continue
                
            self.helper(i, j)
            i += 2*k
            j += 2*k
            
        return "".join(self.input)
    
    def helper(self, i, j):
        for x in range((j+1-i)/2):
            tmp = self.input[i+x]
            self.input[i+x] = self.input[j-x]
            self.input[j-x] = tmp