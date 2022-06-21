# https://leetcode.com/problems/maximize-distance-to-closest-person
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        firstOnePos = None
        lastOnePos = None
        maxConsecutiveZeros = 0
        
        n = len(seats)
        # get the position of the first seated chair
        # this is to seat alex in the first position
        for i in range(n):
            if seats[i] == 1:
                firstOnePos = i
                break
        
        # get the position of the last seated chair
        # this is to seat alex in the last position
        for i in range(n-1, -1, -1):
            if seats[i] == 1:
                lastOnePos = i
                break
        
        # general case
        # if we have arr like 1 0 0 0 0 0 1 0 0 1 --> we want to make alex sit on pos = 3
        # so that he can maximize dist from the seated chairs (1 values)
        # so we need to keep track of max consecutive zeros to get max dist between 1s - call this X
        # so we should seat alex in the middle of X so he's farthest from both surrounding 1s
        count = 0
        for i in range(n):
            if seats[i] == 1:
                count = 0
            else:
                count +=1
                maxConsecutiveZeros = max(maxConsecutiveZeros, count)
        
        d0 = firstOnePos - 0 # dist from first already seated chair if we seat alex at idx 0
        dn = n - 1 - lastOnePos # dist from last already seated chair if we seat alex at the end
        d = (maxConsecutiveZeros + 1)//2 # general case, if we seat alex in between 2 already seated chairs  
        
        return max(d0, dn, d)