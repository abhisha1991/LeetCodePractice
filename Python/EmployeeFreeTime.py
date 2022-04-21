# https://leetcode.com/problems/employee-free-time/
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        timestamp = []
        maxend = 0
        minstart = sys.maxsize
        minend = sys.maxsize
        
        
        # create a timestamp from the schedule where you're capturing intervals of being busy
        for s in schedule:
            # a single employee could be busy more than 1 interval, so capture all this in a flat list
            if type(s) == list:
                for ss in s:
                    timestamp.append((ss.start, ss.end))
                    if ss.end > maxend:
                        maxend = ss.end
                    if ss.start < minstart:
                        minstart = ss.start
                    if ss.end < minend:
                        minend = ss.end
            else:
                timestamp.append((s.start, s.end))
                if s.end > maxend:
                    maxend = s.end
                if s.start < minstart:
                    minstart = s.start
                if s.end < minend:
                    minend = s.end
                    
        # sort the timestamp by start, end time
        timestamp = sorted(timestamp, key=lambda x: (x[0], x[1]))
        
        # this method works, but gives us time limit exceeded
        def method1TLE():
            # for keeping a record of whether someone is busy at a given timestamp
            # notice maxend+1 is the length since we want to capture maxend index 
            busy = [0] * (maxend+1)

            ts = 0
            while ts < len(timestamp):
                cur = timestamp[ts]
                start = cur[0]
                end = cur[1]
                
                for i in range(start, end):
                    busy[i] = 1
                ts +=1

            # we can start iterating from minend, 
            # since that is the first real free interval we may potentially have
            i = minend
            ans = []
            while i < len(busy):
                if busy[i] == 1:
                    i +=1
                    continue

                # now busy[i] == 0, so capture this interval
                start = i
                while i < len(busy) and busy[i] == 0:
                    i +=1

                # now busy[i] is 1 so next job has started
                end = i

                # (3,3) doesnt count as a free interval - it is of size 0
                if start != end and end < len(busy):
                    ans.append(Interval(start, end))
                
                i +=1

            return ans
        
        def method2():
            res = []
            lastend = minend
            for ts in timestamp:
                start = ts[0]
                end = ts[1]
                # [[1,2], [1,3], [4,10], [5,6]]
                # first iteration - last end is 2
                # second iteration - last end is 3
                # third iteration - since start (4) is > lastend (3) ==> (3,4) is free
                if start > lastend:
                    res.append(Interval(lastend, start))
                
                lastend = max(lastend, end)
            
            return res
        
        return method2()