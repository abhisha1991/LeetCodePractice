import sys
# https://www.youtube.com/watch?v=okr-XE8yTO8


class CircularQ(object):
    def __init__(self, size):
        self.size = size
        self.q = [-sys.maxsize] * size
        # -1 index specifies empty queue
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        if self.front == self.rear == -1:
            return True
        return False

    def isFull(self):
        if self.isEmpty():
            return False
        if self.front == (self.rear + 1) % self.size:
            return True

    def enqueue(self, ele):
        # self.printIdx()
        if self.isEmpty():
            # empty queue
            self.rear += 1
            self.front += 1
            self.q[self.rear] = ele
            print("Added element ", ele)
            return

        # add to rear
        if self.isFull():
            print("Cant add elements, we're full. Failed to add ", ele)
            return

        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = ele
        print("Added element ", ele)

    def dequeue(self):
        # self.printIdx()
        if self.isEmpty():
            print("Cannot dequeue from empty queue")
            return

        print("Removing item ", self.q[self.front])
        self.front = (self.front + 1) % self.size

        if self.front == (self.rear + 1) % self.size:
            self.front = self.rear = -1
            # make queue empty

    def printIdx(self):
        print("Front is", self.front)
        print("Rear is", self.rear)

    def print(self):
        if self.isEmpty():
            return
        print("Printing queue content")
        i = self.front
        # if front is less than rear, its a simple display up till rear
        if i <= self.rear:
            while i <= self.rear:
                print(self.q[i])
                i += 1
        else:
            # if we have to wrap around, display till end of array
            while i < self.size:
                print(self.q[i])
                i += 1
            # start with i being 0 and move till rear
            i = i % self.size
            while i <= self.rear:
                print(self.q[i])
                i += 1

    def front(self):
        if self.front != -1:
            return self.q[self.front]
        return None

s = CircularQ(5)
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)
s.enqueue(5)
s.enqueue(6)
s.dequeue()
s.dequeue()
s.dequeue()
s.dequeue()
s.dequeue()
s.dequeue()
s.dequeue()
s.dequeue()
s.enqueue(100)
s.dequeue()
s.enqueue(101)
s.enqueue(102)
s.enqueue(103)
s.enqueue(104)
s.dequeue()
s.dequeue()
s.enqueue(105)
s.enqueue(106)
s.enqueue(107)
s.enqueue(108)
s.printIdx()
s.print()
s.dequeue()
s.dequeue()
s.dequeue()
s.dequeue()
s.dequeue()
s.dequeue()
s.enqueue(4)
s.enqueue(3)
s.enqueue(2)
s.print()
