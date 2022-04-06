# https://www.youtube.com/watch?v=GmpyAMpjpUY
# the above has an excellent explanation to use minheap
# https://leetcode.com/problems/meeting-rooms-ii/
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ts = []
        for i in intervals:
            start = i[0]
            end = i[1]
            # we capture timestamp events, when we add/remove rooms 
            ts.append((start, 1))
            ts.append((end, -1))
        
        ts = sorted(ts, key=lambda x: (x[0], x[1]))
        
        curRooms = 0
        maxRooms = 0
        
        for meeting in ts:
            if curRooms > maxRooms:
                maxRooms = curRooms
            # either add or remove a room based on what event has occurred (start/end)
            curRooms += meeting[1]
        return maxRooms