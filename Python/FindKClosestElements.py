# https://leetcode.com/problems/find-k-closest-elements 
import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        
        # if x is in arr, then left will point to the left element of x
        # if x is not in arr, then left will point to element immediately smaller than x 
        left = bisect.bisect_left(arr, x) - 1
        
        # if x is in arr, then right will point to pos of x
        # if x is not in arr, then right will point to element immediately larger than x
        right = left + 1
        
        # left literally means pos that is left of window start, right literally means pos that is right of window end

        # window is defined from (left+1, right), ie, everything "inclusive" from left+1 to right-1 is going to be returned
        # keep in mind that arr[i:j] means that this slice returned DOES NOT contain arr[j], but DOES contain arr[i]
        # because the bounds of the window are (left+1, right), thus the window size is right - left - 1
        while right - left - 1 < k:
            if left == -1:
                right +=1
                continue
            
            if right == len(arr):
                left -= 1
                continue
            
            if abs(arr[left]-x) <= abs(arr[right]-x):
                # include left element in the window, so expand leftward
                left -=1
            else:
                # include right element in the window, so expand rightward
                right +=1
        
        # window is defined from (left+1, right), so return those elements
        # notice how everything inclusive between left+1 and right-1 is what we are returning
        return arr[left+1: right]