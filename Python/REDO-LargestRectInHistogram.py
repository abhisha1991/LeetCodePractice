# https://leetcode.com/problems/largest-rectangle-in-histogram/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        h = heights
        lenh = len(h)
        '''
        consider running example of 2,1,5,6,2,3
        
                             |
                          |  |
                          |  |
                          |  |     |
                    |     |  |  |  |
                    |  |  |  |  |  |
                -------------------------
             idx    0  1  2  3  4  5
             h[i]   2  1  5  6  2  3
             left   0  0  2  3  2  5
             right  0  5  3  3  5  5
        
        here the significance of left and right is most important
        
        consider a rectangle with height 5, 
        we are trying to store left to be the earliest index that is >=5 without interruption
        we are trying to store right to be the latest index that is >=5 without interruption

        "interruption" here means that there should be consecutive rects with height >=5 for them to be considered
        imagine if you have a rect of height 100 at the end, even then the left and right for rect 5 will NOT change, since 5 has been "interrupted" by h[4] = 2
        
        both left and right are inclusive of the current rect itself, thus rect with height 5 gets left=2, right=3
        
        notice that for rect with height 1 (shortest rect), left = 0 and right = 5, ie, it covers the entire width
        '''
        
        # stack stores indices not heights
        # height can be obtained by doing something like h[stack[-1]]
        stack = []
        
        # left stores the left boundary of a given rectangle at position i
        # right stores the right boundary of a given rectange at position i
        left = [sys.maxsize] * lenh
        right = [sys.maxsize] * lenh
        
        i = 0
        # move left to right
        while i < lenh:
            if i == 0 or not stack:
                stack.append(i)
                left[i] = i
                
                i +=1
                continue
                
            if h[stack[-1]] < h[i]:
                stack.append(i)
                left[i] = i
                i +=1
                continue
            
            # now height of top of stack element is greater than equal to current height
            # so keep popping till you reach a height that is less than current
            while stack and h[stack[-1]] >= h[i]:
                stack.pop()
            
            # now stack top will have an index whose height is less than h[i]
            if stack:
                # left boundary will be immediate rhs nbr of this element which is less than current element
                # hence the +1 to stack top index
                left[i] = stack[-1] + 1
            else:
                left[i] = 0
            
            stack.append(i)
            i +=1
        
        
        # move right to left, re-init variables
        stack = []
        i = lenh-1
        while i > -1:
            if i == lenh-1 or not stack:
                stack.append(i)
                right[i] = i
                
                i -=1
                continue
            
            if h[stack[-1]] < h[i]:
                stack.append(i)
                right[i] = i
                i -=1
                continue
            
            # now height of top of stack element is greater than equal to current height
            # so keep popping till you reach a height that is less than current
            while stack and h[stack[-1]] >= h[i]:
                stack.pop()
                
            # now stack top will have an index whose height is less than h[i]
            if stack:
                # so the right boundary will be stack top element (the one lesser than h[i]) - 1
                # why -1? because that will point to the left nbr of the element who is lesser than h[i]
                right[i] = stack[-1] - 1
            else:
                right[i] = lenh-1
            
            stack.append(i)
            i-=1
        
        maxar = 0
        for i in range(len(h)):
            # why doing the +1 when calculating the width?
            # consider above example, notice rect with height 5, its left and right are both 2 and 3
            # so in order to get width of 2, ie, rect with height 5 and 6, we need to do 3-2+1
            w = (right[i]-left[i] + 1)
            maxar = max(maxar, h[i] * w)
        return maxar