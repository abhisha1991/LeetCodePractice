# https://leetcode.com/problems/design-hit-counter/
class HitCounter:

    def __init__(self):
        self.dic = dict()

    def hit(self, timestamp: int) -> None:
        if timestamp in self.dic:
            self.dic[timestamp] +=1
        else:
            self.dic[timestamp] = 1

    def getHits(self, timestamp: int) -> int:
        hits = 0
        begin = timestamp - 300
        # have a new dictionary to only store the last 300 ticks
        # that way we're not storing things forever in the dictionary and taking up too much space
        # and it reduces number of keys to check against below
        d = dict()
        
        # since this for loop is guaranteed to be running for only 300 steps, it can be considered const
        for i in range(begin+1, timestamp+1):
            if i in self.dic:
                hits += self.dic[i]
                d[i]= self.dic[i]
        
        # re-assign the ticks dictionary to be this new dictionary
        self.dic = d
        return hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)