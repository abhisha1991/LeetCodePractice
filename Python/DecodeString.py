# https://leetcode.com/problems/decode-string
import re
class Solution:
    def decodeString(self, s: str) -> str:
        return self.helper(s)
    
    def helper(self, text):
        # no more text left to expand, ie, all text is already expanded, so return
        if '[' not in text:
            return text

        x = re.search("[0-9]+(\[[a-z]+\])", text)
        # x[0] contains the 0th group of the regex match
        # ie, in a pattern like "3[a]2[bc]", x[0] = 3[a]
        x_wo_bracket = x[0].replace('[', '').replace(']', '')
        
        # extract the num part
        num = ''
        for i in range(len(x_wo_bracket)):
            if (x_wo_bracket[i]).isdigit():
                num += x_wo_bracket[i]
            else:
                break
        
        # convert the num part to an int
        num = int(num)
        
        # extract the pattern part
        pattern = x_wo_bracket[i:]
        # expand the pattern by multiplying by num
        pattern_num = num * pattern
        
        # "3[a]2[bc]" --> after having parsed 3[a] and expanded it as aaa, ensure to replace
        # so that we have aaa2[bc] being passed as the next round of texts
        text = text.replace(x[0], pattern_num)        
        return self.helper(text)
        
        
        