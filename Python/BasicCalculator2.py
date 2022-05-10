# https://leetcode.com/problems/basic-calculator-ii
# all operators (+, -, *, /) but no paranthesis
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        op = ['/', '*', '+', '-']

        # if input is like "1"        
        if s.isdigit():
            return int(s)
        
        def getRightNum(s, idx, returnWithoutSign=False):
            # find second num
            second = ''
            j = idx + 1
            neg = False
            if s[j] == '-':
                neg = True
                j +=1

            while j < len(s) and s[j] not in op:
                second += s[j]
                j +=1

            second = int(second)
            if neg:
                second = -second
            
            if returnWithoutSign:
                return abs(second)
            
            return second
        
        def getLeftNum(s, idx, returnWithoutSign=False):
            # find first num
            first = 0
            j = idx - 1
            neg = False
            p = 0
            while j >= 0 and s[j] not in op:
                first += int(s[j]) * 10**p
                p +=1
                j -=1

            if j >=0 and s[j] == '-':
                neg = True
            if neg:
                first = -first
            
            if returnWithoutSign:
                return abs(first)
            
            return first
        
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                continue
            else:
                # it is an operator
                assert(s[i] in op)
                if stack:
                    first = stack.pop()
                else:
                    first = getLeftNum(s, i, True)
                
                second = getRightNum(s, i, True)
                
                # if operators are div or mul, we want to eagerly calculate and ingest on stack top
                if s[i] in ['*', '/']:
                    if s[i] == '*':
                        res = first * second
                    else:
                        res = int(first / second)
                    stack.append(res)
                else:
                    # operator is addition or subtraction, we want to evaluate this lazily
                    # because there may be additional div or mul ahead in the string (BODMAS)
                    
                    # if sign is negative, then just ingest -ve of second num into stack
                    # why? because "2+5-3" ==> [2, 5, -3] and we can just return the sum of the stack
                    # we're summing the stack and that's fine because 2+5-3 is the same as 2 + 5 + (-3)
                    if s[i] == '-':
                        second = -1 * second
                    # order is important here in terms of insertion into stack
                    # because we want second to be top of stack
                    stack.append(first)
                    stack.append(second)
        
        return sum(stack)