# https://leetcode.com/problems/minimum-time-difference
from collections import defaultdict
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def getTotalMins(ts):
            hr = ts.split(":")[0]
            mins = ts.split(":")[1]
            
            return int(hr) * 60 + int(mins)
        
        # if there are duplicate time stamps, then the min diff is 0
        # [12:30, 04:40, 12:30] -- min diff is 0, ie, 12:30 - 12:30
        if len(set(timePoints)) != len(timePoints):
            return 0
        
        dic = defaultdict(list)
        for tp in timePoints:
            mins = getTotalMins(tp)
            '''
            if tp is 12:30
            1st element in value arr stores time from 00:00 hours, ie, 12 x 60 + 30 = 750
            2nd element in value arr stores time to reach next day 00:00 horus, ie, 1440 - 750 = 690
            '''
            dic[tp] = [mins, 1440 - mins]
            
        def getDiff(ts1, ts2):
            ts1 = dic[ts1]
            ts2 = dic[ts2]
            '''
            consider 2 timestamps
            12:30 --> [750, 690]
            22:00 --> [1320, 120]
            
            now the "continuous" diff between these can be either:
            120 + 750 (get 22:00 to reach next day 00:00 and take 00:00 to 12:30)
            or
            1320 - 750 (00:00 to 22:00 minus 00:00 to 12:30)
            
            consider another case (special)
            23:59 --> [1439, 1]
            00:05 --> [5, 1435]
            continuous difference between these will be 1 + 5 
            (ie, reach next day 00:00 from 23:59 and go from 00:00 to 00:05)
            '''
            return min(ts1[0] + ts2[1], ts1[1] + ts2[0], abs(ts1[0] - ts2[0]))
        
        # sort time points, since it allows us to locate nearby timestamps close to each other
        tps = sorted(timePoints)
        
        minDiff = min(getDiff(tps[0], tps[1]), getDiff(tps[-1], tps[-2]), getDiff(tps[0], tps[-1]))
        
        for i in range(1, len(tps)-1):
            cur = tps[i]
            prev = tps[i-1]
            nxt = tps[i+1]
            
            # always take min between cur, prev and cur, nxt
            minDiff = min(minDiff, getDiff(cur, prev))
            minDiff = min(minDiff, getDiff(cur, nxt))
        
        return minDiff