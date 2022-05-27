# https://leetcode.com/problems/maximum-number-of-visible-points
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        
        def angleBetweenEastDirAndPoint(point):
            x1, y1 = location
            x2, y2 = point
            height = y2-y1
            width = x2-x1
            '''
                 me
                 *---------------                 
                 *   /
                  \ / <--- angle 'a'
                   \
                    \    
                     *p
            '''
            # tan is sin/cos => height/width, which is the order of the inputs in atan2
            # atan2 gives answer in radian, so we need to convert to degrees
            # remember pi/2 radian = 90 degrees, so 1 radian is 180/pi, so we multiply radian by 180/pi
            # why use atan2? atan = gives angle value between -90 and 90; atan2 = gives angle value between -180 and 180 
            # since the point can go beyond -90 to 90 degrees, ie, point can lie anywhere on the circle
            # thus, we need to cover the full circle coverage, -180 to 180
            a = math.atan2(height, width) * (180/math.pi)
            if a >=0:
                return a
            else:
                # convert to positive, so -45 degrees from me becomes -45 + 360 = 315 anticlockwise
                return a + 360
        
        n = len(points)
        # exclude all points that are at the location where we are standing
        points = [p for p in points if p != location]
        pointsOnMyLocation = n - len(points)
        
        # if all the points were located where we are standing, we can always see all points from any angle we rotate
        if not points:
            return pointsOnMyLocation    
        
        angles = [angleBetweenEastDirAndPoint(p) for p in points]
        # why sort? because we dont care about specific position of point in points arr
        # we want to be able to compare angle[i] with angle[j] and points i,j will be closer to each other if they're
        # sorted to begin with
        angles.sort()
        
        # extend angles [0, 40, 355] -> [0, 40, 355, 360, 400, 715]
        # why? if we didnt extend, then points like 0 and 355 will appear to be very far away 
        # but in reality 355 is right below 0, so it would be nice to represent 0 in another way, such as 0 + 360
        # such that when we compare 355 and 360, they appear close!
        # no need to sort again, since we're adding a const to a sorted array
        angles += [a + 360 for a in angles]
        
        # last step - sliding window!
        i = 0 
        j = 0 
        
        # max number of points you can see is initially 0
        pointsICanView = 0
        
        # i and j are the "lines" formed between me and p1 and me and p2
        # where p1 and p2 are points in the angles arr 
        while j < len(angles):
            # keep expanding window, ie, increment j
            while (j < len(angles)) and (angles[j] - angles[i] <= angle):
                j +=1
            
            # the window size of points seen so far is j-i
            pointsICanView = max(pointsICanView, j-i)
            
            # at this point angles[j] - angles[i] > angle
            # so now we want to shrink the window from the other end so that we can reach back window expansion condition
            # ie, angles[j] - angles[i] <= angle
            
            # keep contracting window, ie, increment i 
            while (j < len(angles)) and (i < j) and (angles[j] - angles[i] > angle):
                i +=1
        
        return pointsOnMyLocation + pointsICanView