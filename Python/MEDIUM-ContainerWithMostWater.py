# https://leetcode.com/problems/container-with-most-water/description/
# watch this video - https://www.youtube.com/watch?v=cdRaaEYk6tI
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxar = 0
        i = 0
        n = len(height)
        j = n-1
        while i < j:
            width = j-i
            
            # area is capped by min of the 2 heights
            ar = min(height[i], height[j]) * width
            if ar > maxar:
                maxar = ar
            
            # which one should we update, i or j
            # depends on which of the 2 heights were shorter
            # we want to always strive for longer heights (so we can capture more area), 
            # so the shorter side index is updated
            if height[i] > height[j]:
                j -=1
            else:
                i +=1
                
        return maxar