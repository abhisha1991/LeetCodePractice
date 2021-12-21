#https://leetcode.com/problems/to-lower-case/description/
class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        str = list(str)
        for i in range(len(str)):
            if str[i] >= 'A' and str[i] <= 'Z':
                str[i] = chr(ord(str[i]) + 32)
        
        print(str)
        return ''.join(str)