# https://leetcode.com/problems/convert-to-base-2/
class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        res = []
        x = N
        # watch this for negative number binary rep: 
        # https://www.youtube.com/watch?v=4qH4unVtJkE
        while x:
            print("x is " +str(x))
            print("x >> 1 is " +str(x>>1))
            res.append(x & 1)
            print(str.format("res is {}", res))
            x = -(x >> 1)
        return "".join(map(str, res[::-1] or [0]))