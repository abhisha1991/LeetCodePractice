#https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lst=[]
        for i in range (left, right+1):
            check = True
            for digit in str(i):
                if digit == '0':
                    check = False
                    break
                elif i % int(digit) !=0:
                    check = False
            if check == True:
                lst.append(i)
        return lst
