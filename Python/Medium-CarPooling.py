# based off this: https://leetcode.com/problems/car-pooling/discuss/317611/C%2B%2BJava-O(n)-Thousand-and-One-Stops
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        # people in location (persons) = # of people at each km that the car will need carry if there's a stop, default is 0 
        # 1001 as max start and end index can be 1000
        # 0 <= trips[i][1] < trips[i][2] <= 1000

        persons = [0] * 1001
        for t in trips:
            passengers = t[0]
            start = t[1]
            end = t[2]
            persons[start] += passengers # add cap at loc at start index as people are loading
            persons[end] -= passengers # subtract cap at loc at end index as people are getting off
        
        cur = 0
        for i in persons:
            if cur > capacity:
                return False
            cur += i
        return True

class Solution2:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # have a timestamp array
        ts = []
        
        # for each trip, 
        # for the start timestamp, have positive passenger count
        # for the end timestamp, have negative passenger count
        for t in trips:
            # here we register start/end as separate entries in the array
            # this is a common pattern
            ts.append([t[1], t[0]])
            ts.append([t[2], -t[0]])
        
        # sort by timestamp, then by num passengers
        # why? consider the case [[4,5,6],[6,4,7],[4,3,5],[2,3,5]] and capacity = 13
        # this trip is actually possible if we remove people at point 5 on the x axis
        # first before we add people to the car
        # if we didn't sort by num passengers post timestamp, you'll notice that 
        # we tend to add people given how ts is sorted, which results in a "false" value
        ts = sorted(ts, key=lambda x: (x[0], x[1]))
        
        # current capacity
        cap = 0
        for trip in ts:
            cap += trip[1]
            if cap > capacity:
                return False
        return True