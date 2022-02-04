# see min stack problem for inspiration
class MaxStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack == []:
            self.stack.append([x, x])
        else:
            prev = self.stack[-1]
            # store every stack element as [value, max_so_far]
            # this is the key point
            # in a stack, say if we have [5,7,2,3] -- max is 7 up to element 3
            # so the idea is that along with element addition in stack, we store "max up to that top of stack" element
            # so we store the above like [[5,5], [7,7], [2,7], [3,7]] -- 1st element is val, 2nd element is max element so far 
            self.stack.append([x, max(prev[1], x)])

    def pop(self) -> int:
        if self.stack == []:
            return None
        last = self.stack.pop()
        return last[0]

    def top(self) -> int:
        if self.stack == []:
            return None
        last = self.stack[-1]
        # 1st element is value itself
        return last[0]

    def peekMax(self) -> int:
        if self.stack == []:
            return None
        last = self.stack[-1]
        # 2nd element is "max so far"
        return last[1]

    def popMax(self) -> int:
        max_element = self.peekMax()
        popped = self.pop()
        add_back = []
        # keep popping elements till max element is reached
        # store the non max elements to add back later to preserve the stack
        while popped < max_element:
            add_back.append(popped)
            popped = self.pop()
            
        # add back non max elements that you popped in reversed order of popping
        # consider an example to convince yourself on why adding back in reverse makes sense
        for ele in reversed(add_back):
            self.push(ele)
        
        # popped that didn't match while condition must be largest current element
        return popped


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()