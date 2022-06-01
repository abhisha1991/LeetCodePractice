# https://leetcode.com/problems/rle-iterator/

# gives memory limit exceeded, because we are eagerly expanding the list up front, which it doesn't like
class RLEIterator2:

    def __init__(self, encoding: List[int]):
        self.count = -1
        self.enc = []
        for i in range(0, len(encoding), 2):
            c = encoding[i]
            v = encoding[i+1]
            
            self.enc.extend([v] * c)

    def next(self, n: int) -> int:
        self.count += n
        if self.count >= len(self.enc):
            return -1
        
        return self.enc[self.count]

class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        # idx will point to freq, whereas idx + 1 will point to the actual element who corresponds to freq 'idx'
        self.idx = 0
    
    def next(self, n: int) -> int:
        # if n is larger than the frequency of the current element, 
        # located at even index of the encoding array - ie, self.encoding[self.idx] 
        # then decrement n by this frequency and move to the next element's frequency
        while self.idx < len(self.encoding) and n > self.encoding[self.idx]:
            n -= self.encoding[self.idx]
            # move to the next element, by making idx move forward by 2 units (since the format is given as [freq1, num1, freq2, num2])
            self.idx += 2
        
        if self.idx >= len(self.encoding):
            return -1
        
        # decrement current element's freq by n and return element at idx + 1
        self.encoding[self.idx] -= n
        return self.encoding[self.idx + 1]

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)