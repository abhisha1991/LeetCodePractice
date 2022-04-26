# https://leetcode.com/problems/plates-between-candles/
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        # indices are initialized with -1
        l2rCandleIdx = [-1] * n
        r2lCandleIdx = [-1] * n
        plates = [0] * n
        
        # l2r contains indices of the last seen candle from the left
        for i in range(n):
            if s[i] == '|':
                l2rCandleIdx[i] = i
            else:
                if i > 0 and l2rCandleIdx[i-1] != -1:
                    l2rCandleIdx[i] = l2rCandleIdx[i-1]
        
        # r2l contains the indices of the last seen candle from the right
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                r2lCandleIdx[i] = i
            else:
                if i < n-1 and r2lCandleIdx[i+1] != -1:
                    r2lCandleIdx[i] = r2lCandleIdx[i+1]
        
        # this contains the cumulative count of the number of plates left to right (prefix sum)
        for i in range(n):
            if i > 0 and s[i] == '*':
                plates[i] = plates[i-1] + 1
            elif i > 0 and s[i] == '|':
                plates[i] = plates[i-1]
            elif i == 0 and s[i] == '*':
                plates[i] = 1
        
        res = []
        
        for q in queries:
            s = q[0]
            e = q[1]
            
            # right is going to hold an index pointing to the nearest left candle position frpm pos 'e'
            # left is going to hold an index pointing to the nearest right candle position from pos 's'
            # so in effect left and right are extreme positions of candles within the query bounds (s,e)
            right = l2rCandleIdx[e]
            left = r2lCandleIdx[s]
            
            # if right or left indices are invalid, then append 0
            if right == -1 or left == -1 or right < left:
                res.append(0)
            else:
                # plates[right] is holding the total number of plates seen from left so far, at pos 'right'
                # plates[left] is holding the total number of plates seen from left so far, at pos 'left'
                # since right and left are indices of nearest right and left candles
                # so the difference will give the number of plates between left and right
                res.append(plates[right] - plates[left])
        
        return res