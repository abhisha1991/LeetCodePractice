# similar problem to koko eating bananas
# https://leetcode.com/problems/koko-eating-bananas/
# https://leetcode.com/problems/cutting-ribbons/
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        l = 1 # smallest ribbon length
        r = max(ribbons) # largest ribbon length
        
        res = 0
        # binary search on potential ribbon lengths
        while l <= r:
            m = (l+r)//2 # mid ribbon length (integer value)
            count = 0
            for x in ribbons:
                count += int(x/m)
                
            if count >= k:
                # update res to be max ribbon length seen so far
                res = max(res, m)
                l = m+1
            else:
                r = m-1
        return res