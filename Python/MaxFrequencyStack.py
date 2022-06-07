# https://leetcode.com/problems/maximum-frequency-stack/
from collections import defaultdict
class FreqStack:
    '''
    push 5 5 5 5 5 3 3 3 2 2 2 1
    group = 5:[5] 4: [5] 3: [5,3,2] 2:[5,3,2] 1 : [5,3,21] maxfreq=5
    1st pop 5:[] 4: [5] 3: [5,3,2] 2:[5,3,2] 1 : [5,3,21] maxfreq=4
    2nd pop 5:[] 4: [] 3: [5,3,2] 2:[5,3,2] 1 : [5,3,21] maxfreq=3
    3rd pop 5:[] 4: [] 3: [5,3] 2:[5,3,2] 1 : [5,3,21] maxfreq=3
    4th pop 5:[] 4: [] 3: [5] 2:[5,3,2] 1 : [5,3,21] maxfreq=3
    5th pop 5:[] 4: [] 3: [] 2:[5,3,2] 1 : [5,3,21] maxfreq=2 and so on...
    '''
    def __init__(self):
        self.num2freq = defaultdict(int) # stores key as number, value as freq 
        self.group = defaultdict(list) # for a given freq, what are the numbers
        self.mf = 0 # max freq

    def push(self, val: int) -> None:
        self.num2freq[val] +=1
        freq = self.num2freq[val]
        
        self.mf = max(self.mf, freq)
        self.group[freq].append(val)

    def pop(self) -> int:
        # pop from the max freq group
        x = self.group[self.mf].pop()
        # reduce the freq of this popped element
        self.num2freq[x] -=1
        
        # if nothing is left in the group anymore with max freq
        # then go one level down in freq
        if not self.group[self.mf]:
            self.mf -=1
        
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()