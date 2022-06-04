# https://leetcode.com/problems/valid-perfect-square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        low = 2
        # sqrt(num) is always less than num/2, so instead of setting higher limit to num-1, set it to int(num/2)
        high = num//2
        while low <= high:
            mid = (low + high)//2
            sq = mid * mid
            if sq == num:
                return True
            if sq < num:
                low = mid + 1
            else:
                high = mid - 1
        return False