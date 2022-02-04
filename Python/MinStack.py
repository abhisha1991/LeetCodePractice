# https://leetcode.com/problems/min-stack/submissions/
class MinStack:
    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append([val, val])
        else:
            prev = self.stack[-1]
            # store every stack element as [value, min_so_far]
            # this is the key point
            # in a stack, say if we have [5,7,2,3] -- min is 2 up to element 3
            # so the idea is that along with element addition in stack, we store "min up to that top of stack" element
            # so we store the above like [[5,5], [7,5], [2,2], [3,2]] -- 1st element is val, 2nd element is min element so far 
            self.stack.append([val, min(val, prev[1])])

    def pop(self) -> None:
        if self.stack == []:
            return
        self.stack.pop()

    def top(self) -> int:
        last = self.stack[-1]
        return last[0]

    def getMin(self) -> int:
        last = self.stack[-1]
        return last[1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()