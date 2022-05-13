# https://leetcode.com/problems/design-log-storage-system/
class LogSystem:

    def __init__(self):
        self.arr = []
        
    def put(self, id: int, timestamp: str) -> None:
        self.arr.append((timestamp, id))
    
    def getYear(self, ts):
        return ts.split(':')[0]
    
    def getMonth(self, ts):
        return ts.split(':')[1]
    
    def getDay(self, ts):
        return ts.split(':')[2]
    
    def getHour(self, ts):
        return ts.split(':')[3]
    
    def getMinute(self, ts):
        return ts.split(':')[4]
    
    def getSecond(self, ts):
        return ts.split(':')[5]
    
    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        g = ["Year", "Month", "Day", "Hour", "Minute", "Second"]
        assert(granularity in g)
        start = [self.getYear(start), self.getMonth(start), self.getDay(start), 
                 self.getHour(start), self.getMinute(start), self.getSecond(start)]
        
        end = [self.getYear(end), self.getMonth(end), self.getDay(end), 
                 self.getHour(end), self.getMinute(end), self.getSecond(end)]
        
        # slice corresponds to the slice idx where we will slice our start/end
        # example, if granularity is month, then we want to slice start as start[:2]
        slicets = [i+1 for i in range(len(g))]
        # get the index of month in 'g', ie, 1
        idx = g.index(granularity)
        # get slice index, which will be 2 for month
        sliceIdx = slicets[idx]
        
        start = start[:sliceIdx]
        end = end[:sliceIdx]
        
        res = []
        for a in self.arr:
            ts = [self.getYear(a[0]), self.getMonth(a[0]), self.getDay(a[0]), 
                 self.getHour(a[0]), self.getMinute(a[0]), self.getSecond(a[0])]
            
            ts = ts[:sliceIdx]
            tslen = len(ts)
            if ''.join(start) <= ''.join(ts) <= ''.join(end):
                res.append(a[1])

        return res
    
# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)