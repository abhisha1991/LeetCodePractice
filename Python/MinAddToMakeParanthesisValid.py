# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        
        ans = 0
        i = 0
        # if string starts with close paranthesis, keep adding to ans since we'd need to add open paranthesis to counter act
        while i < len(s) and s[i] == ')':
            ans +=1
            i +=1
        
        stack = []
        # at this point, i points to an open paranthesis
        while i < len(s):
            if s[i] == '(':
                stack.append(i)
            else:
                # encoutered a closed paranthesis
                # balance out with open paranthesis that are there in stack
                if stack:
                    stack.pop()
                else:
                    # if not stack means that we've run out of open paranthesis but are still encountering closed paranthesis
                    # excess closing paranthesis means we need to add open paranthesis, ie, increment ans
                    ans +=1
            i +=1
        
        # add closing paranthesis to any excess open paranthesis in the stack
        ans += len(stack)
        return ans