# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        i = 0
        while i < (len(tokens)):
            # evaluate regular positive integers like "50", and negative integers like "-50"
            if tokens[i].isdigit() or (len(tokens[i]) > 1 and tokens[i][0] == '-' and tokens[i][1:].isdigit()):
                stack.append(int(tokens[i]))
                i +=1
                continue
            
            # else the token is a operator
            op = tokens[i]
            
            # if its an commutative operator like + or *
            if op in ['+', '*']:
                if op == '+':
                    res = stack.pop() + stack.pop()
                else:
                    res = stack.pop() * stack.pop()
                
                # remember to add result on top of stack
                stack.append(res)
            
            # non commutative operator
            elif op in ['-', '/']:
                second = stack.pop()
                first = stack.pop()
                if op == '-':
                    stack.append(first - second)
                else:
                    # truncate division to lower
                    stack.append(int(first/second))
            
            i +=1
        
        return stack[0]