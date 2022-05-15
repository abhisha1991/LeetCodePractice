# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        
        ans = 0
        i = 0
        while i < len(s) and s[i] == ')':
            ans +=1
            i +=1
        
        stack = []
        while i < len(s):
            if s[i] == '(':
                stack.append(i)
            else:
                # balance out with open paranthesis that are there in stack
                if stack:
                    stack.pop()
                else:
                    # excess closing paranthesis means we need to add open paranthesis, ie, increment ans
                    ans +=1
            i +=1
        
        # add closing paranthesis to any excess open paranthesis in the stack
        ans += len(stack)
        return ans