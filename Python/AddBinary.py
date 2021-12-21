#https://leetcode.com/problems/add-binary/submissions/ 
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return self.solve2(a, b)
        # return self.solve(a, b)
    
    def solve2(self, a, b):        
        lena, lenb = len(a), len(b)
        # do padding with 0s
        if lena > lenb:
            b = "0" * (lena - lenb) + b
            lenb += lena-lenb
        elif lenb > lena:
            a = "0" * (lenb - lena) + a
            lena += lenb-lena 
        
        # after this point lena and lenb should be same
        print(a)
        print(b)
        i = lena - 1
        ans = []
        carry = 0
        while i >= 0:
            s = int(a[i]) + int(b[i]) + carry
            if s < 2:
                ans.insert(0, s)
                carry = 0
            else:
                ans.insert(0, s % 2)
                carry = 1
            i -=1
            
        if carry:
            ans.insert(0, 1)
            
        return "".join([str(i) for i in ans])
    
    def solve(self, a, b):    
        inta = int(a,2)
        intb = int(b,2)
        s = inta + intb
        # bin(s) always returns the binary string with prefix, "0b", hence, if we do index 2 onwards, we will have our required string
        return str(bin(s)[2:])