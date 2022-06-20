# https://leetcode.com/problems/my-calendar-i
class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, start: int, end: int) -> bool:
        for event in self.arr:
            s = event[0]
            e = event[1]
            
            # if existing interval overlaps partially with the new incoming interval
            # or if existing interval is completely contained in the incoming interval
            # then there is an overlap
            if (s <= start < e or s < end < e) or (start <= s <= e <= end):
                return False
        
        self.arr.append([start, end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)