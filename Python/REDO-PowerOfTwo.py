# http://practice.geeksforgeeks.org/problems/power-of-2/0

class Solution(object):
    def powerOfTwo(self, n):
        if n == 1:
            return True
        if n % 2 == 1:
            return False
        s = n
        while s > 2:
            if s % 2 == 1:
                return False
            s = s / 2
        if s == 2:
            return True
        else:
            return False

    def isPowerOfTwo(self, n):
        return n > 0 and ((n & (n - 1)) == 0)
    # example, 4 = 100 and 3 = 011 ==> 4&3 = 000 = 0
    # example, 5 = 101 and 4 = 100 ==> 5&4 = 100, which is 4, not 0

s = Solution()
s.powerOfTwo(10)