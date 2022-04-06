# https://leetcode.com/problems/merge-intervals/submissions/    
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        res = []
        while len(intervals) > 1:
            cur = intervals.pop(0)
            nxt = intervals.pop(0)
            # cur = [a,b] and nxt = [c,d]
            
            # a < c and b < c -- no merge
            if cur[0] < nxt[0] and cur[1] < nxt[0]:
                res.append(cur)
                # insert nxt back to the intervals at 0 position
                # so nxt has a chance to be cur next iteration
                # and has the chance to merge with other future intervals
                intervals.insert(0, nxt)
                continue
            
            # a <= c <= b, then new interval is [min(a,c), max(b,d)]
            # we know "c" is always greater than equal to "a" (sorted intervals)
            # so just choose "a" by default for lower limit
            if cur[0] <= nxt[0] and nxt[0] <= cur[1]:
                intervals.insert(0, [cur[0], max(cur[1], nxt[1])])
        
        # there is a single interval remaining in intervals
        # pop and add to res
        res.append(intervals.pop())
        return res