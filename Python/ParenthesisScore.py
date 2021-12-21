# https://leetcode.com/problems/score-of-parentheses/

class Solution(object):
    def __init__(self):
        self.stack = []
        
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        self.stack = [0]
        for c in S:
            if c == "(":
                self.stack.append(0)
            else:
                last = self.stack.pop()
                self.stack[-1] += max(2 * last, 1)
        return self.stack[-1]

'''
https://leetcode.com/problems/score-of-parentheses/discuss/141828/Python-and-Javascript-simple-and-readable-Stack-solution

Based off the above

Imagine if you have (()(()))
(1 (()))
(1 (1))
(1 2)
(3)
=6

The idea is that every time we see a (, we add a 0 to the stack
then every time we see a ), then we pick the last element, last = stack[-1]
and pick the max between 2*last and 1
we add this result to the new stack head (which is 2nd from last original head)

So in the above the stack would look like
[0]  -- originally we start with 1 stack with 1 element
[0, 0] - first ( is evaluated
[0, 0, 0] - second ( is evaluated
[0, 1] - third element is evaluated, which is )
[0, 1, 0] - fourth element, ie, ( is evaluated
[0, 1, 0, 0] - fifth element, ie, ( is evaluated
[0, 1, 1] - sixth element, ie, ) is evaluated
[0, 3] - seventh element, ie, ) is evaluated
[6] - eigth element, ie ) is evaluated

last element of stack, ie 6 is returned

'''