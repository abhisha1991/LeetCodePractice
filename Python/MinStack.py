# https://leetcode.com/problems/min-stack/submissions/
class MinStack(object):
    def __init__(self):
        self.stack = []
        # holds minimum elements of the stack. 
        # Top will always be most min element, 2nd from top is 2nd most min element and so on
        self.minst = []
        
    def push(self, x):
        # if we dont have a minimums at all or our min most element is > element being inserted (x)
        if not self.minst or self.getMin() >= x:
            self.minst.append(x)
            
        self.stack.append(x)
                
    def pop(self):
        # only if the top most element being popped from original stack is the min most element
        # only then does the min most element get updated
        if self.stack and self.minst and self.stack[-1] == self.getMin():
                self.minst = self.minst[:-1]
            
        if self.stack:
            self.stack = self.stack[:-1]

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        if self.minst:
            return self.minst[-1]
        return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()