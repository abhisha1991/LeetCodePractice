# https://leetcode.com/problems/basic-calculator
# this one contains paranthesis and + and - only
class Solution:
    def calculate(self, s: str) -> int:
        # we add () to the string's ends to actually trigger an evaluation
        # notice how we call an evaluation command only when we encounter a paranthesis, 
        # so if input had no paranthesis - say it was 7-8+9, then we would never evaluate it 
        s = "(" + s + ")"
        s = s.replace(" ", "")
        # if we are going to use stack, we process elements from right to left, which we don't want to do
        # imagine processing 7-8+9 from right to left, we first evaluate 8+9=17 and then we evaluate 17-7=10
        # which is the wrong answer! we rather need to evaluate 7-8 first and then -1+9=8
        # thus we reverse the list, so that we are processing elements in the stack in the "correct" left to right order
        s = list(reversed(s))
        stack = []
        op = ["+", "-", "*", "/"]
        
        def evaluate(operator, num1, num2):
            if operator == '+':
                return num1 + num2
            elif operator == '-':
                return num1 - num2
            elif operator == "*":
                return num1 * num2
            elif operator == "/":
                assert(num2 != 0)
                return num1/num2
        
        i = 0
        while i < len(s):
            # the ) is actually an OPEN bracket! recall reversing the list
            if s[i] == ')':
                stack.append(s[i])
                i +=1
                continue
            
            # if s[i] is a digit, find the entire number and add to stack
            if s[i].isdigit():
                j = 0
                num = int(s[i]) * 10**j
                i +=1
                while i < len(s) and s[i].isdigit():
                    j +=1
                    num += int(s[i]) * 10**j
                    i +=1
                
                stack.append(num)
            
            # if s[i] is an operator, then add to stack
            if i < len(s) and s[i] in op:
                stack.append(s[i])
                i +=1
                continue
            
            # the ( is actually a CLOSE bracket! recall reversing the list
            # the CLOSE bracket actually triggers an evaluate function call
            if s[i] == '(':
                ele = []
                while stack and stack[-1] != ')':
                    # -2 + 1 --> in this case stack is [')', 1, '+', 2, '-']
                    # so we can have a negative sign in front, to signify negative number, so we need to take care of this
                    ele.append(stack.pop())
                    if ele[0] == '-':
                        ele.pop()
                        if stack:
                            n = stack.pop()
                            assert(type(n) == int)
                            ele.append(-n)
                    
                    # this can happen in the last calculation
                    # example (7 - 8 + 9) --> )9 + 8 - 7( --> last bracket encountered --> )9 + -1 --> )8
                    # at this stage, we pop 8 from stack and add 8 to ele and now stack[-1] is )
                    # so we just want to pop this last ) and break out of the loop, so we can ultimately add 8 to top of stack
                    if stack and stack[-1] == ')':
                        # remove the front bracket
                        stack.pop()
                        break
                        
                    # get 3 elements in ele
                    while len(ele) < 3:
                        ele.append(stack.pop())
                    
                    # assert middle element is operator
                    # assert surrounding elements are nums
                    assert(ele[1] in op)
                    assert(type(ele[2]) == int)
                    assert(type(ele[0]) == int)
                    
                    val = evaluate(ele[1], ele[0], ele[2])
                    stack.append(val)
                    
                    # reset ele for next operation
                    # for example (7 - 8 + 9) is evaluated as 9 + 8 - 7, so after doing 7-8 =-1 and adding this "val" to stack
                    # we need to reset ele, so that we can do 9 + (-1) next time
                    ele = []
                    
                
                if ele:
                    assert(len(ele) == 1)
                    stack.append(ele[0])
                
                i +=1
                continue
            
        return stack[-1]