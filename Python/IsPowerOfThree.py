class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        elif n % 3 == 0:
            n = n / 3
            return self.isPowerOfThree(n)
        return False
            