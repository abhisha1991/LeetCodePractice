# https://leetcode.com/problems/exam-room/
class ExamRoom:

    def __init__(self, n: int):
        self.arr = []
        self.n = n
        
    def seat(self) -> int:
        if not self.arr:
            self.arr.append(0)
            return 0
        
        # STEP 1: FIND MAX DIST BETWEEN 2 EXISTING PEOPLE
        
        # at this point we know arr has at least 1 element
        # this is handling the cases where we seat the person at the first pos or the last pos
        # ie, when there is only 1 person in the arr
        maxDist = max(self.arr[0] - 0, self.n - 1 - self.arr[-1])
        
        # why len-1? because we want to get i th and i+1 th points
        # to compare 2 people's dist
        for i in range(len(self.arr)-1):
            # general case dist 'd' - the mid point between any 2 consecutive points
            d = (self.arr[i+1] - self.arr[i]) // 2
            
            maxDist = max(maxDist, d)
        
        # STEP 2: SEAT INCOMING PERSON BETWEEN THE MAX DIST BETWEEN 2 PEOPLE
        
        # special case: if there is only 1 person in the arr not at the first pos 
        # 0 0 0 P --> then seat new person P' at pos 0, ie, P' 0 0 P 
        
        # example: this may happen if we seat at 0, seat at n, then 0 pos leaves
        # then we need to place the new person coming in at the 0 pos
        if self.arr[0] == maxDist:
            self.arr.insert(0, 0)
            return 0
        
        # general case, there are 2 people who are seated, so seat incoming person between them
        # why len-1? because we want to get i th and i+1 th points to compare 2 people
        for i in range(len(self.arr)-1):
            curDist = (self.arr[i+1] - self.arr[i]) // 2
            
            if curDist == maxDist:
                # we need to find pos where to place this person which will be the average point
                # between where the i+1 th and i th person are sitting
                idxSeat =  (self.arr[i+1] + self.arr[i]) // 2
                # we need to insert that seat index at pos i+1
                self.arr.insert(i+1, idxSeat)
                return idxSeat
        
        # special case: person has not been seated in pos 0, nor in the general case
        # so seat him last at the last pos
        self.arr.append(self.n-1)
        return self.n-1

    def leave(self, p: int) -> None:
        self.arr.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)