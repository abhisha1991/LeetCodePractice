# https://leetcode.com/problems/my-calendar-ii/
from collections import defaultdict
class MyCalendarTwo:

    def __init__(self):
        self.pos = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.pos[start] += 1
        self.pos[end] -= 1
        
        keys = sorted(self.pos.keys())
        counter = 0
        canAdd = True
        
        for i in keys:
            counter += self.pos[i]
            if counter > 2:
                canAdd = False
        
        if not canAdd:
            # restore state of dictionary
            self.pos[start] -= 1
            self.pos[end] += 1
        
        return canAdd
        
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)