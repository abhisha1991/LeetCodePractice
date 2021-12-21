import math


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        maxnum = int(math.pow(2, 31) - 1)
        if dividend == 0:
            return 0
        if divisor == 0:
            return maxnum
        '''
        a/b = e(log a) / e(log b) = e(log a - log b)
        '''
        sign = 1
        if dividend < 0 and divisor < 0:
            pass
        elif dividend > 0 and divisor > 0:
            pass
        else:
            sign = -1

        ans = math.exp(math.log(abs(dividend)) - math.log(abs(divisor)))
        if sign is -1:
            ans = int('-' + str(int(ans)))
        else:
            ans = int(ans)

        if ans > maxnum:
            return maxnum
        return ans
