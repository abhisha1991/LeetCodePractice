# https://leetcode.com/problems/container-with-most-water/description/
# watch this video - https://www.youtube.com/watch?v=cdRaaEYk6tI
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        points = []
        for i in range(length):
            points.append((i + 1, height[i]))

        maxa = 0
        i = 0  # left pointer
        j = length - 1  # right pointer
        # while left and right dont meet
        while i < j:
            # find length
            l = abs(points[i][0] - points[j][0])
            # find min height of the 2 points
            h = min([points[i][1], points[j][1]])
            # max container area = length x height
            area = l * h
            if maxa < area:
                maxa = area
            # if left side is smaller, increase left pointer
            if points[i][1] < points[j][1]:
                i += 1
            else:
                # if right side is smaller, increase right pointer
                j -= 1

        return maxa

