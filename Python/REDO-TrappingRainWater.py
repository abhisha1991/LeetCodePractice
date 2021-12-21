# https://www.youtube.com/watch?v=KV-Eq3wYjxI
# https://leetcode.com/problems/trapping-rain-water/description/
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lenh = len(height)
        if lenh <= 2:
            return 0

        maxhleft = [0] * lenh
        maxhright = [0] * lenh
        res = 0
        # we model this problem such that we try to find the height of water units above each tower and add up each of them,
        # rather than trying to find area between 2 towers separated by dist x
        # how much water is above a given tower?
        # we look left and right and find the max height towers we can find, we pick the min height of the 2, say this is 'h'
        # now we do h - our own tower's height, if this is negative, it means we are taller than our chosen neighbor 'h',
        # so there can be no water above us and hence we choose 0
        # if we are smaller than 'h' then we can store (h - current height) units of water

        # use dynamic programming to figure out maxhleft and right in linear time
        # maxhleft for us will be either our current height or the maxhleft just to our left
        maxhleft[0] = height[0]
        for i in range(1, lenh):
            maxhleft[i] = max([maxhleft[i - 1], height[i]])

        maxhright[lenh - 1] = height[lenh - 1]
        for i in range(lenh - 2, -1, -1):
            maxhright[i] = max([maxhright[i + 1], height[i]])

        for i in range(lenh):
            res += max(min(maxhleft[i], maxhright[i]) - height[i], 0)

        return res