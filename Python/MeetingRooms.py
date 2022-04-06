# https://leetcode.com/problems/meeting-rooms/
# arr is a list of start and end times
# example input: [[0,30],[5,10],[15,20]]
# here there is overlap that is happening, so a person cannot attend all 3 meetings without overlap
# so return ans as false

# another input: [[7,10],[2,4]]
# return true because person can attend both meetings

# identical to carpooling problem
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        ts = []
        for i in intervals:
            start = i[0]
            end = i[1]
            # 2nd num in tuple is whether a person is entering (+1) or exiting (-1) a meeting
            ts.append((start, 1))
            ts.append((end, -1))
        
        # sort timestamp by asc time and by asc order of capacity 
        ts = sorted(ts, key=lambda x: (x[0], x[1]))
        
        countMeet = 0
        for meeting in ts:
            if countMeet > 1:
                return False
            countMeet += meeting[1]
        return True

# alternate solution would be to do MergeIntervals.py function
# get the length of the stack, if that is lesser in length than the input length, it means we have merged an interval 
# ==> there is overlap, so return false. If the length is the same, return true