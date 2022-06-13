class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1 = sorted(slots1, key = lambda x: x[0])
        slots2 = sorted(slots2, key = lambda x: x[0])
        
        n1 = len(slots1)
        n2 = len(slots2)
        i = 0
        j = 0
        
        while i < n1 and j < n2: 
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]
            
            # if interval doesn't overlap and interval 1 is the limiting (smaller) one
            # then increment index for interval 1
            if s2 >= e1:
                i +=1
                continue
            
            # if interval doesn't overlap and interval 2 is the limiting (smaller) one
            # then increment index for interval 2
            if s1 >= e2:
                j +=1
                continue
            
            # if the intervals are large enough to hold the duration inside them individually
            if e1 - s1 >= duration and e2 - s2 >= duration:
                # at this point s1 < e2 and s2 < e1
                # as we established above in the if conditions
                # if the minimum overlap happens to be greater than duration
                if min(e2 - s1, e1 - s2) >= duration:                  
                    # take the limiting start point of the 2 start points and add duration to it to get result interval
                    s = max(s1, s2)
                    return [s, s + duration]
            
            # increment criteria for whichever interval is lagging behind
            if e1 < e2:
                i +=1
            else:
                j +=1
        
        return []