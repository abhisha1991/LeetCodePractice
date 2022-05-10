# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        
        slist = list(s)
        # replace all open and close paranthesis by an empty char
        for i in range(len(slist)):
            if slist[i] == '(' or slist[i] == ')':
                slist[i] = ''
        
        # holds a pair of indices per element of matched '(' and ')'
        # (idx1, idx2) - 
        # idx1 refers to pos of matched '('
        # idx2 refers to pos of matched ')'
        paranthesis = []
        
        for i in range(len(s)):
            # attach both value, ie, paranthesis and its corresponding index to stack
            if s[i] == '(':
                stack.append((s[i], i))
            if s[i] == ')':
                # if we are currently on ')' and have encountered a '(' on top of stack
                # then store the indices of the open and close paranthesis valid pair in list
                if stack and stack[-1][0] == '(':
                    val, idx = stack.pop()
                    paranthesis.append((idx, i))
        
        # go through all valid pairs of paranthesis and replace in slist
        for p in paranthesis:
            v1, v2 = p
            slist[v1] = '('
            slist[v2] = ')'
            
        return ''.join(slist)