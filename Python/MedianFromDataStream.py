import heapq

class MinHeap():
    def __init__(self, xList):
        self.heap = xList
        heapq.heapify(self.heap)

    def insert(self, val):
        print(f"Inserting val into minheap: {val}")
        heapq.heappush(self.heap, val)
    
    def peekMin(self):
        # print(f"Peeking min element: {self.heap[0]}")
        return self.heap[0]
    
    def deleteMin(self):
        print("Deleting min element...")
        return heapq.heappop(self.heap)

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
        print(f"Inserting val into maxheap: {val}")
        heapq.heappush(self.heap, -val)

    def peekMax(self):
        # print(f"Peeking max element: {-self.heap[0]}")
        return -self.heap[0]
    
    def deleteMax(self):
        print("Deleting max element...")
        # remember to multiply by -1 because the number inside was
        # implemented based on minheap 
        return -1 * heapq.heappop(self.heap)
    
    def print(self):
        print(f"Heap is {[-x for x in self.heap]}")

        
class MedianFinder:

    def __init__(self):
        self.hmax = MaxHeap([])
        self.hmin = MinHeap([])

    def addNum(self, num: int) -> None:
        if len(self.hmax.heap) == 0 or num < self.hmax.peekMax():
            self.hmax.insert(num)
        else:
            self.hmin.insert(num)
            
        # balance the 2 heaps
        if len(self.hmax.heap) > len(self.hmin.heap) + 1:
            e = self.hmax.deleteMax()
            self.hmin.insert(e)
        
        elif len(self.hmin.heap) > len(self.hmax.heap) + 1:
            e = self.hmin.deleteMin()
            self.hmax.insert(e)
            

    def findMedian(self) -> float:
        mnhsize = len(self.hmin.heap)
        mxhsize = len(self.hmax.heap)
        n = mnhsize + mxhsize
        if n % 2 == 1:
            if mnhsize > mxhsize:
                return self.hmin.peekMin()
            else:
                return self.hmax.peekMax()
        else:
            n1 = self.hmax.peekMax()
            n2 = self.hmin.peekMin()
            return (n1+n2)/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()