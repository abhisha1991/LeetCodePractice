#https://leetcode.com/problems/remove-outermost-parentheses/submissions/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        v=0
        result = ''
        for i in range(len(S)):
            if S[i] == '(':
                count +=1
            elif S[i] == ')':
                count -=1
                if count == 0:
                    result += (S[v+1:i])
                    v = i+1
        return result
