# https://leetcode.com/problems/largest-rectangle-in-histogram/

# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28902/5ms-O(n)-Java-solution-explained-(beats-96)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        len_bars = len(heights)
        if len_bars == 0:
            return 0
        if len_bars == 1:
            return heights[0]
        
        area = 0
        lessfl = ['#'] * len_bars 
        lessfl[0] = -1
        lessfr = ['#'] * len_bars
        lessfr[-1] = len_bars
        
        for i in range(1, len_bars):
            p = i-1
            
            while p >= 0 and heights[p] >= heights[i]:
                p = lessfl[p]
            
            lessfl[i] = p
        
        for i in range(len_bars-2, -1, -1):
            p = i+1
            
            while p < len_bars and heights[p] >= heights[i]:
                p = lessfr[p]
            
            lessfr[i] = p
        
        
        for i in range(0, len_bars):
            area = max(area, heights[i] * (lessfr[i] - lessfl[i] - 1))
        
        return area

# sub optimal solution (o n square)
class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        len_bars = len(heights)
        if len_bars == 0:
            return 0
        if len_bars == 1:
            return heights[0]
        
        start = 0
        end = len_bars - 1
        curr = 0
        area = 0
        curr_results = dict()
        
        while curr < len_bars:
            width = 1
            curr_height = heights[curr]
            ar = 0
            
            i = curr - 1
            prev_same = False
            # if prev is same as curr height, then area is same as prev
            if i >=0 and heights[i] == curr_height:
                prev_same = True
                ar = curr_results[i]
            
            if not prev_same:
                # front pass
                i = curr + 1
                while i <= end:
                    if curr_height <= heights[i]:
                        width +=1
                        i +=1
                    else:
                        break
                
                # back pass
                i = curr - 1
                while i >= start:        
                    if curr_height <= heights[i]:
                        width +=1
                        i -=1
                    else:
                        break
                    
                ar = width * curr_height
                
            curr_results[curr] = ar
            curr +=1
             
            area = max(area, ar)
        
        #print(curr_results)
        return area