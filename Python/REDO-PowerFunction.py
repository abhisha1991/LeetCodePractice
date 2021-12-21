# https://leetcode.com/problems/powx-n/description/
# implement x^n


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1

        if n == 1:
            return x

        # this was an important condition, what if n is less than 0
        if n < 0:
            # remember to make n as -n because now you've transferred the negative to 'x'
            n = -n
            x = 1 / x

        if n % 2 == 0:
            n = int(n / 2)
            return self.myPow(x * x, n)
        else:
            n = int(n / 2)
            # important condition - if n is odd, it would be the same as x * n-even case
            return x * self.myPow(x * x, n)
