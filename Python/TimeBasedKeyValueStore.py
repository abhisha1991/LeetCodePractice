# https://leetcode.com/problems/time-based-key-value-store/
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = [(value, timestamp)]
        else:
            self.dic[key].append((value, timestamp))
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        
        # first index in dic[key] is the element index
        # second index can be 0 or 1, 0 == actual value stored, 1 == timestamp corresponding to that value
        if timestamp < self.dic[key][0][1]:
            return ""
        
        i = -1
        while timestamp < self.dic[key][i][1]:
            i -=1
        
        return self.dic[key][i][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)