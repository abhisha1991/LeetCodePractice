class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        m = len(num1)
        n = len(num2)
        vals = [0] * (m+n)
        # say we were doing 99 x 99 = 9801, at max result can be of 4 digits 
        
        # go from right to left for each number
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                n1 = ord(num1[i]) - ord('0') # get the integer value by doing ascii subtraction
                n2 = ord(num2[j]) - ord('0')
                
                # say we're doing 14 x 22, so len(vals) is 4. So to access last pos, ie, index 3
                # we need to do i+j+1 because it will be m-1 + n-1 + 1, m=2, n=2 ==> 2-1 + 2-1 + 1
                # this is because we subtract 1 twice!
                s = vals[i+j+1] + (n1 * n2)
                
                # this holds the carry (say 6 x 3 = 18, so this will store 1)
                vals[i+j] += int(s/10)
                # this holds the non-carry (for 6 x 3 = 18, this will store 8)
                vals[i+j+1] = s%10
        
        # remove leading 0s
        while vals[0] == 0:
            vals.pop(0)
            
        # convert vals to string
        res = ''
        for i in vals:
            res += str(i)
        
        return res