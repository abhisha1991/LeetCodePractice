# https://leetcode.com/problems/construct-the-rectangle/submissions/
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        w = int(math.sqrt(area))
        while area % w > 0:
            w -=1
        return [int(area/w),w]

'''
The key insight is that we need to start with the square root
suppose the area was 100
we know that 100 can be obtained as follows:
1 x 100
2 x 50
4 x 25
5 x 20
10 x 10

but we know that the closest numbers that when multiplied give 100, will be available 
near the sq.root of the number, because by definition, sq.root gives a number, which when 
multiplied by itself (a "close" number) gives the product

'''