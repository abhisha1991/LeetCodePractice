# https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python
# This is a file that uses direct heap functionality in python, so we don't have to build it from scrach
import heapq

class MinHeap():
    def __init__(self, xList):
        self.heap = xList
        heapq.heapify(self.heap)

    def insert(self, val):
        print(f"Inserting val: {val}")
        heapq.heappush(self.heap, val)
    
    def peekMin(self):
        print(f"Peeking min element: {self.heap[0]}")
        return self.heap[0]
    
    def deleteMin(self):
        print("Deleting min element...")
        heapq.heappop(self.heap)

    def print(self):
        print(f"Heap is {self.heap}")

# python only has implementation for minheap
# so max heap is implemented as -1 * minheap val
# so we have to create an abstraction to mask this
class MaxHeap():
    def __init__(self, xList):
        xList = [-x for x in xList]
        self.heap = xList
        heapq.heapify(self.heap)
    
    def insert(self, val):
        print(f"Inserting val: {val}")
        heapq.heappush(self.heap, -val)

    def peekMax(self):
        print(f"Peeking max element: {-self.heap[0]}")
        return -self.heap[0]
    
    def deleteMax(self):
        print("Deleting max element...")
        heapq.heappop(self.heap)
    
    def print(self):
        print(f"Heap is {[-x for x in self.heap]}")

print("*** Going to init MIN heap ***")

s = MinHeap([5,6,10,3,5,8,3,9,43])
s.print()
s.insert(2)
s.print()
s.peekMin()
s.insert(1)
s.print()
s.peekMin()
s.deleteMin()
s.print()
s.deleteMin()
s.deleteMin()
s.print()

print()
print("*** Going to init MAX heap ***")

s = MaxHeap([5,6,10,3,5,8,3,9,43])
s.print()
s.insert(200)
s.print()
s.peekMax()
s.insert(100)
s.print()
s.peekMax()
s.deleteMax()
s.print()
s.deleteMax()
s.deleteMax()
s.print()