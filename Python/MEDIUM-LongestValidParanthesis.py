'''
https://leetcode.com/problems/longest-valid-parentheses
In this approach, we make use of two counters left and right. 

First, we start traversing the string from the left towards the right and for every ( encountered, we increment the left counter and for every ) encountered, we increment the right counter. 

Whenever left becomes equal to right, we calculate the length of the current valid string and keep track of maximum length substring found so far. 
If right becomes greater than left we reset left and right to 0.

Next, we start traversing the string from right to left and similar procedure is applied.
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0
        
        left = 0 # number of left brackets
        right = 0 # number of right brackets
        maxlen = 0 # overall max length
        length = 0 # current session length
        
        # left to right scan
        for i in range(len(s)):
            if s[i] == '(':
                left +=1                
            else:
                right +=1
            
            # session length is always increased no matter what
            length +=1
            if left == right:
                maxlen = max(length, maxlen)
            
            # we never expect right brackets to exceed left, if so, we have reached an invalid sub-string
            if right > left:
                length = 0
                left = 0
                right = 0
        
        # reset vars for right to left scan
        length = 0
        left = 0
        right = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left +=1
            else:
                right +=1
            
            # session length is always increased no matter what
            length +=1
            if left == right:
                maxlen = max(length, maxlen)
            
            # we never expect left brackets to exceed right, if so, we have reached an invalid sub-string
            if left > right:
                length = 0
                left = 0
                right = 0
        
        return maxlen