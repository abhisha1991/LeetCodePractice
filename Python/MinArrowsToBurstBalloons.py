import sys
import operator
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 2:
            return len(points)
        
        points.sort(key=operator.itemgetter(0))
        # stores number of arrows to be shot. You will atleast shoot 1 arrow
        # why? because <2 length of points has already been checked
        # so there are atleast 2 points, so you'll need at least 1 arrow
        res = 1 
        minend = sys.maxsize
        for p in range(0, len(points)):
            curr = points[p]
            # if start of current balloon is more than minend, then a new cluster is made
            # so shoot an arrow to eliminate the old cluster, ie, increment res
            if curr[0] > minend:
                res +=1 # shoot at the minend to kill the entire cluster
                minend = curr[1] # update new cluster's end as minend
            else:
                # there is an overlap, curr belongs to same active cluster
                # this new balloon "curr" can be handled by the same arrow 
                # when we kill the other previous balloons in the cluster
                # we're capped by the min of the end of all balloons in the cluster as 
                # it is at pos "minend" where we will shoot the arrow to kill the cluster
                minend = min(minend, curr[1])
        return res