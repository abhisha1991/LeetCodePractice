# https://leetcode.com/problems/different-ways-to-add-parentheses/
class Solution:
    def __init__(self):
        self.cache = dict()
    
    def evaluate(self, m, n, op):
        if op == "+":
            return m+n
        if op == "-":
            return m-n
        if op == "*":
            return m*n
        
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            # if the expression is a multi digit number, say 78, this handles that as well
            # converts it to an int
            # why return a list, because we need to perform iteration over the result
            # as seen in objects 'left' and 'right' below
            return [int(expression)]
        if expression in self.cache:
            return self.cache[expression]
        res = []
        for i in range(len(expression)):
            # if curr char is operator, get left and right and evaluate
            if expression[i] in ['+', '*', '-']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                # do an evaluation across each element of left and right
                # this is the equivalent of saying that place a paranthesis at each pos of elemnts in left/right
                for l in left:
                    for r in right:
                        op = expression[i]
                        ans = self.evaluate(l, r, op)
                        res.append(ans)
                
        self.cache[expression] = res
        return res                        