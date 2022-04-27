# https://leetcode.com/problems/flip-string-to-monotone-increasing/
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        
        l2r = [0] * (n+1) # cumulative number of 1s found l2r that we need to flip to make 0 
        r2l = [0] * (n+1) # cumulative number of 0s found r2l that we need to flip to make 1
        
        '''
        we offset both l2r and r2l by 1 index when calculating this prefix sum
        
        S = "010110": 
        we have l2r = [0, 0, 1, 1, 2, 3, 3] --> notice how we have an extra 0 in front pos
        we have r2l = [2, 2, 1, 1, 1, 0, 0] --> notice how we have an extra 0 in last pos
        
        and total is  [2, 2, 2, 2, 3, 3, 3]
        so min(total) = 2
        
        so we need 2 flips to make this 000111, ie, flip pos 1 and last pos
        '''
        
        # notice how we start at 1 since we're looking back at prev state to fill ourselves
        for i in range(1, n+1):
            if s[i-1] == '1':
                l2r[i] = l2r[i-1] + 1
            else:
                l2r[i] = l2r[i-1]
        
        # notice how we start at n-2 since we're looking ahead at forward state to fill oursleves
        for i in range(n-2, -1, -1):
            if s[i+1] == '0':
                r2l[i] = r2l[i+1] + 1
            else:
                r2l[i] = r2l[i+1]
        
        total = [0] * (n+1)
        for i in range(n+1):
            total[i] = l2r[i] + r2l[i]
        
        return min(total)