# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem
class MyQueue(object):
    def __init__(self):
        # stack1 actually contains the elements
        self.stack1 = []
        self.stack2 = []

    def peek(self):
        if len(self.stack2) > 0:
            peek = self.stack2[len(self.stack2) - 1]
            print("Peeked element is: ", peek)
            return peek
        if len(self.stack1) == 0:
            return None
        peek = self.stack1[0]
        print("Peeked element is: ", peek)
        return peek

    def pop(self):
        if len(self.stack2) > 0:
            val = self.stack2[len(self.stack2) - 1]
            self.stack2 = self.stack2[:-1]
            return val

        i = len(self.stack1) - 1
        if i == -1:
            return None

        if i == 0:
            val = self.stack1[0]
            self.stack1 = []
            self.stack2 = []
            return val

        while len(self.stack1) >= 2:
            self.stack2.append(self.stack1[i])
            self.stack1 = self.stack1[:-1]
            i -= 1

        val = self.stack1[0]
        self.stack1 = []

        return val

    def put(self, value):
        self.stack1.append(value)


queue = MyQueue()
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
print("Popped element is", queue.pop())
queue.peek()
queue.put(5)
print("Popped element is", queue.pop())
print("Popped element is", queue.pop())
queue.peek()
print("Popped element is", queue.pop())
queue.peek()
print("Popped element is", queue.pop())

print("End of first attempt")
queue.put(1)
print("Popped element is", queue.pop())
queue.put(2)
queue.put(3)
queue.peek()
queue.put(4)
print("Popped element is", queue.pop())
queue.put(5)
queue.put(6)
queue.put(7)
queue.put(8)
queue.peek()
print("Popped element is", queue.pop())
print(queue.stack1)
print(queue.stack2)
'''
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
'''
