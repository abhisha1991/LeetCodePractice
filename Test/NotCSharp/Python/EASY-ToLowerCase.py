#https://leetcode.com/problems/to-lower-case/

class Solution:
    def toLowerCase(self, str: str) -> str:
        s = 0
        new_lst = []
        for a in list(str):
            s = ord(a)
            if 65<= s <=96 :
                new_lst.append(chr(s+32))
            else:
                new_lst.append(a)
        return "".join(new_lst)
