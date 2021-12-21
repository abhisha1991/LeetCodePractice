# https://leetcode.com/problems/longest-valid-parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i in range(0, len(s)):
            if s[i] == "(":
                # append index of open paranthesis
                stack.append(i)
            else:
                # we are able to find a match
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        
        # at this point, stack contains idxes of "breaking points" - where we broke a valid paranthesis substring
        # there are gaps between the indexes, whose diff represents a valid paranthesis substring
        # so we need to find longest valid paranthesis substring
        # which is the difference between 2 consecutive elements in the stack
        # so return longest difference between 2 consecutive elements in the stack 

        # if stack is empty, whole string is valid
        if not stack:
            return len(s)
        
        maxlen = 0
        
        # set j to be the end and find max length of substring from j to top of stack
        j = len(s)
        
        while stack:
            i = stack.pop() 
            maxlen = max(maxlen, j-i-1)
            # make top of stack as the new "end of string"
            j = i
            
        return max(maxlen, j)