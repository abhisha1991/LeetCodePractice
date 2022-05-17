# https://leetcode.com/problems/add-strings/
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1 == '0':
            return num2
        
        if num2 == '0':
            return num1
        
        diff = abs(len(num1) - len(num2))
        # make the 2 lengths for num1 and num2 to be the same
        if diff > 0:
            if len(num1) > len(num2):
                num2 = "0" * diff + num2
            else:
                num1 = "0" * diff + num1
        
        arr = [0] * (len(num1) + 1) 
        for i in range(len(num1)-1, -1, -1):
            n1 = int(num1[i])
            n2 = int(num2[i])
            
            # n3 is going to be current digits sum along with prev carry
            n3 = n1 + n2 + arr[i+1]
            if n3 > 9:
                r = n3 % 10
                c = int(n3/10)
            else:
                r = n3
                c = 0
            
            # remainder part gets overriden completely
            # since we already considered the remainder when calculating n3
            arr[i+1] = r
            
            # carry part
            # replace either a 0 or 1 depending on what the carry was
            arr[i] = c
            
        while arr:
            if arr[0] == 0:
                arr.pop(0)
            else:
                break
        
        arr = [str(i) for i in arr]
        return ''.join(arr)