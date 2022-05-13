# https://leetcode.com/problems/can-place-flowers
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        fb = flowerbed
        if fb == [0] and n == 1:
            return True
        
        count = 0
        for i in range(0, len(fb)):
            # optimization, early return
            if count >= n:
                return True
            
            # first index is special
            if i == 0:
                if fb[i] == 0 and fb[i+1] == 0:
                    fb[i] = 1
                    count +=1
            
            # general case, if there are no neighbors who have flowers placed on them
            # then we can place a flower
            elif i < len(fb)-1 and fb[i] == 0 and fb[i-1] == 0 and fb[i+1] == 0:
                fb[i] = 1
                count +=1
                
            # last index is special
            elif i == len(fb)-1:
                if fb[i] == 0 and fb[i-1] == 0:
                    fb[i] = 1
                    count +=1
                    
        if count >= n:
            return True
        
        return False