# https://www.youtube.com/watch?v=KV-Eq3wYjxI
# https://leetcode.com/problems/trapping-rain-water/description/

# we model this problem such that we try to find the height of water units above each tower and add up each of them,
# rather than trying to find area between 2 towers separated by dist x
# how much water is above a given tower?
# we look left and right and find the max height towers we can find, we pick the min height of the 2, say this is 'h'
# now we do h - our own tower's height, if this is negative, it means we are taller than our chosen neighbor 'h',
# so there can be no water above us and hence we choose 0
# if we are smaller than 'h' then we can store (h - current height) units of water

# use dynamic programming to figure out maxhleft and maxright in linear time
class Solution:
    def trap(self, height: List[int]) -> int:
        lenh = len(height)
        
        # if there are only 2 buildings or less, water will flow to its sides
        if lenh <=2:
            return 0
        
        maxleft = [0] * lenh
        maxright = [0] * lenh
        
        # note we're starting from idx 1, ie, 2nd building, maxleft for 1st building is 0
        for i in range(1, len(maxleft)):
            maxleft[i] = max(height[i-1], maxleft[i-1])
            
        # for maxright, go from right to left, stepping by -1 (leftward)
        # we start from 2nd from last building
        # for last building, maxright would be 0
        for i in range(len(maxright)-2, -1, -1):
            maxright[i] = max(height[i+1], maxright[i+1])
        
        total = 0
        # go through every building and look at its left and right tallest nbors
        for i in range(len(height)):
            l_nbor_maxh = maxleft[i]
            r_nbor_maxh = maxright[i]
            curr = height[i]
            # find out units of water above your current building
            # 3 cases:
            # curr is tallest amongst your "tallest" nbors, in which case water_trapped_above_curr = 0, ie, min_margin < 0
            # l_nbor_maxh is taller than r_nbor_maxh, and both taller than curr, so limited by right side
            # r_nbor_maxh is taller than l_nbor_maxh, and both taller than curr, so limited by left side
            min_margin = min([l_nbor_maxh - curr, r_nbor_maxh - curr])
            water_trapped_above_curr = max([0, min_margin])
            
            total += water_trapped_above_curr
            
        return total