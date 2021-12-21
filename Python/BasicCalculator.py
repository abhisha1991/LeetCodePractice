# https://leetcode.com/problems/basic-calculator-ii/discuss/
class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(s)
        try:
            y = int(s)
            if type(y) == int:
                return y
        except:
            pass

        first = ''
        second = ''
        s = s.replace(' ', '')
        if '/' in s:
            op = '/'
        elif '*' in s:
            op = '*'
        elif '+' in s:
            op = '+'
        elif '-' in s:
            op = '-'
        else:
            raise Exception("op not found")
        idx = s.index(op)

        # right number
        for i in range(idx + 1, len(s)):
            if s[i] >= '0' and s[i] <= '9':
                second += s[i]
            else:
                break

        # left number
        for i in range(idx - 1, -1, -1):
            if s[i] >= '0' and s[i] <= '9':
                first += s[i]
            else:
                break

        first = first[::-1]
        first = int(first)
        second = int(second)

        if op == '/':
            res = first / second
            res = int(res)
        elif op == '*':
            res = first * second
        elif op == '+':
            res = first + second
        elif op == '-':
            res = first - second

        # first op second -> res
        find = str(first) + op + str(second)
        s = s.replace(find, str(res))
        print("Find is", find)
        print("Res is", res)
        print("s is", s)
        self.calculate(s)