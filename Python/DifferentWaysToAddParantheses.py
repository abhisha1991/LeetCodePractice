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
            return [int(expression)]
        if expression in self.cache:
            return self.cache[expression]
        res = []
        for i in range(len(expression)):
            # if curr char is operator, get left and right and evaluate
            if expression[i] in ['+', '*', '-']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        op = expression[i]
                        ans = self.evaluate(l, r, op)
                        res.append(ans)
                
        self.cache[expression] = res
        return res