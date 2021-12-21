# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        ele = ['(', '{', '[']
        notele = [')', '}', ']']
        if s[0] in notele:
            return False
        for i in s:
            if i in ele:
                stack.append(i)
            elif len(stack) > 0:
                e = stack[-1]
                stack = stack[0:len(stack) - 1]
                if e == '(' and i != ')':
                    return False
                if e == '{' and i != '}':
                    return False
                if e == '[' and i != ']':
                    return False
            else:
                return False
        if len(stack) > 0:
            return False
        return True