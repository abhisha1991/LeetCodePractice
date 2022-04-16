# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k >= n:
            return sum(cardPoints)
        
        window = n - k
        s = sum(cardPoints)
        # cur is the current window sum
        cur = sum(cardPoints[:window])
        
        maxSum = s - cur
        i = 1
        j = window
        while j < n:
            # sliding window - remove from left, add from right
            cur = cur - cardPoints[i-1] + cardPoints[j]
            # everything minus window is the set of cards you can pick
            if s - cur > maxSum:
                maxSum = s - cur
            i +=1
            j +=1
        
        return maxSum