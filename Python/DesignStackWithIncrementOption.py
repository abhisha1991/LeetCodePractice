# https://leetcode.com/problems/design-a-stack-with-increment-operation
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) >= self.maxSize:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        if k > len(self.stack):
            k = len(self.stack)
        
        # can also just simply increment bottom k, ie, range(0,k) values for stack list and return
        # but that would be cheating since a stack cannot access elements from the bottom
        
        res = []        
        topN = len(self.stack) - k
        
        i = topN
        len_stack = len(self.stack)
        
        # get top n elements as is
        while topN > 0:
            x = self.stack.pop()
            res.append(x)
            topN -=1
        
        # for the remaining bottom elements, add val
        while i < len_stack:
            x = self.stack.pop()
            res.append(x + val)
            i +=1
        
        # remember to reverse the list!
        self.stack = list(reversed(res))



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)