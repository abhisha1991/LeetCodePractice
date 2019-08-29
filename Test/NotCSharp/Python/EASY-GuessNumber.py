# https://leetcode.com/problems/guess-number-higher-or-lower/
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binsearch(0, n)
    
    def binsearch(self, start, end):
        if start <= end:
            mid = int((start + end)/2)
            num = guess(mid)
            if num == 0:
                return mid
            elif num == 1:
                return self.binsearch(mid+1, end)
            elif num == -1:
                return self.binsearch(start, mid-1)