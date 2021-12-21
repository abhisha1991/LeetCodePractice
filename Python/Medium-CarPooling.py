# based off this: https://leetcode.com/problems/car-pooling/discuss/317611/C%2B%2BJava-O(n)-Thousand-and-One-Stops
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        
        # people in location (pil) = # of people at each km that the car will need carry if there's a stop, default is 0 
        # 1001 as max start and end index can be 1000
        # 0 <= trips[i][1] < trips[i][2] <= 1000

        pil = [0] * 1001
        for t in trips:
            #1 is the start index of trip
            #2 is the end index of trip
            pil[t[1]] += t[0] #add cap at loc at start index as people are loading
            # at any point people at a location cant exceed capacity
            if pil[t[1]] > capacity:
                return False
            pil[t[2]] -= t[0] #subtract cap at loc at end index as people are getting off
        
        tmpcap = 0
        for i in pil:
            if tmpcap > capacity:
                return False
            tmpcap += i
        return True