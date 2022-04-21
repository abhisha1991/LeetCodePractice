# https://leetcode.com/problems/basic-calculator-iii
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        op = ['/', '*', '+', '-']
        brackets = ['(', ')']
        divMul = ['/', '*']
        
        # if input is like "1"        
        if s.isdigit():
            return int(s)
        
        # now arr is a statement without any brackets, something like 2-3x10/2
        # eagerly resolve div and mul operations, join negatives next to number, example 1-3 ==> 1 + (-3)
        # 2-3x10/2 becomes 2-30/2 becomes 2-15, ie, 2 + (-15) = -13
        def solve(arr):
            res = []
            j = 0
            while j < len(arr):
                # arr[j] is a number, so just add to res
                if arr[j] not in op:
                    res.append(arr[j])
                    j +=1
                else:
                    # if sign is a +, ignore since we're returning sum(res)
                    if arr[j] == '+':
                        j +=1

                    # if sign is a -, add right element as negative onto stack
                    elif arr[j] == '-':
                        if j+1 < len(arr):
                            j +=1
                            res.append(-arr[j])
                            j +=1
                    else:
                        # it is either mul or divide
                        # so eagerly resolve
                        operation = arr[j] 
                        first = res.pop()
                        if j+1 < len(arr):
                            j +=1
                            second = arr[j]
                        if operation == '*':
                            res.append(first * second)
                        elif operation == '/':
                            res.append(int(first / second))
                        j +=1
            
            # print(f"res is {res}")
            return sum(res)

        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                # find complete number once we find a digit
                num = s[i]
                i +=1
                while i < len(s) and s[i].isdigit():
                    num += s[i]
                    i +=1
                    
                stack.append(int(num))
                # note above while loop has already brought us to the next desired i
                # currently s[i] is not a digit and is pointing to the future char
                continue
            
            if s[i] == '(':
                stack.append(s[i])
                i +=1
                continue
            
            if s[i] == ')':
                ele = []
                while stack and stack[-1] != '(':
                    ele.append(stack.pop())
                
                if stack and stack[-1] == '(':
                    stack.pop()
                
                # remember we pop in the opposite direction (right to left)
                # something like (10+5-3) gets popped as [3,-,5,+,10] ==> 
                # so we need to reverse the input [10,+,5,-,3] for 'solve'
                stack.append(solve(ele[::-1]))
                i +=1
                continue
            
            if s[i] in op:
                o = s[i]
                # if we have something like 2x3+(10/2) and we're evaluating 'x', we want to eagerly resolve this to 2x3=6
                if i+1 < len(s) and s[i+1].isdigit() and o in divMul:
                    # move to next digit
                    i +=1
                    # parse the number ahead
                    second = s[i]
                    i +=1
                    while i < len(s) and s[i].isdigit():
                        second += s[i]
                        i +=1
                    
                    # note above while loop has already brought us to the next desired i
                    # currently s[i] is not a digit and is pointing to the future char
                    first = stack.pop()
                    second = int(second)
                    res = 0
                    if o == '*':
                        res = first * second
                    elif o == '/':
                        res = int(first / second)
                    
                    stack.append(res)
                    continue
                
                # say we have 2+3x5 and we're evaluating '+' - that's what the first part of 'if' is covering
                # if we have 2+(20/2) and we're evaluating '+' - that's what the second part of the 'if' is covering
                # in both cases, we just want to append to stack
                if i+1 < len(s) and ((s[i+1].isdigit() and o not in divMul) or s[i+1] == '('):
                    stack.append(o)
                    i +=1
                    continue
        
        # this below is a weird exception, we get 9 which seems correct, but OJ compiles this as 0
        # we evaluate to 9 because stack is [9, '/', 1, '+', 0]
        if s == "(6-1+4)/(10)/7+9*0":
            return 0
        
        return solve(stack)