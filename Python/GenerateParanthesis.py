# https://leetcode.com/problems/generate-parentheses/description/
class Solution:
    def __init__(self):
        self.arr = []
        self.res = []
    # follows very similar code compared to AllSubsets
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        '''

        '''
        self.arr = [None] * 2 * n
        self.arr[0] = '('
        self.arr[2 * n - 1] = ')'
        self.helper(0, n)
        return self.res

    def helper(self, c, n):
        if c == 2 * n - 2:
            if self.isvalid():
                self.res.append(''.join(self.arr))
        else:
            x = c + 1
            if x == 2 * n - 1:
                return
            self.arr[x] = '('
            self.helper(x, n)

            self.arr[x] = ')'
            self.helper(x, n)

    def isvalid(self):
        stack = []
        for i in self.arr:
            if i == '(':
                stack.append('(')
            else:
                if len(stack) == 0:
                    return False
                l = len(stack)
                stack = stack[0: l - 1]
        if len(stack) != 0:
            return False
        return True