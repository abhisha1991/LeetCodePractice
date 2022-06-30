# https://leetcode.com/problems/angle-between-hands-of-a-clock
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minuteAngle = (minutes/60 * 360)
        # this part is important, if its 3:35 
        # then not only has the hour hand moved 90 degrees, ie, 3 * 30
        # but it has moved slightly more, which is by 35/60 * 30
        # why are we multiplying by 30? because each hour in a clock represents 30 degrees (12 x 30 = 360)
        hourAngle = (hour % 12 + minutes/60) * 30
        
        diff1 = abs(hourAngle - minuteAngle)
        diff2 = abs(360 - diff1)
        diff = min(diff1, diff2)
    
        return diff