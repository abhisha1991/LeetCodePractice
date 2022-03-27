# full explanation given in MaxHeap.py
# see that file for more details
class Solution():
    def __init__(self):
        self.heap = ['#']
        self.size = 0

    def parent(self, child):
        return int(child/2)
    
    def leftChild(self, parent):
        return parent * 2
    
    def rightChild(self, parent):
        return parent * 2 + 1

    def peekMin(self):
        return self.heap[1]
    
    def swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def print(self):
        print("Heap so far is...")
        for i in range(1, self.size+1):
            print(self.heap[i])

    def insert(self, val):
        print(f"Inserting val: {val}")
        self.heap.append(val)
        self.size +=1
        self.heapify()
        self.print()
    
    def removeMin(self):
        if self.size == 0:
            return None
        
        ele = self.heap[1]
        print(f"Going to remove min element: {ele}")
        self.swap(1, self.size)
        self.size -=1
        self.heap.pop()
        
        self.heapify()
        self.print()
    
    def heapify(self):
        if self.size < 2:
            return
        
        child = self.size
        while child > 1:
            parent = self.parent(child)
            left = self.leftChild(parent)
            right = self.rightChild(parent)

            if child != left and child != right:
                raise Error("something went wrong")
            
            if right > self.size:
                if self.heap[child] < self.heap[parent]:
                    self.swap(child, parent)
                child = parent
                continue
            
            if self.heap[left] < self.heap[right]:
                child = left
            else:
                child = right
            
            if self.heap[child] < self.heap[parent]:
                self.swap(child, parent)
            child = parent
                
s = Solution()
s.removeMin()
s.insert(10)
s.insert(20)
s.insert(1)
s.insert(9)
s.insert(7)
s.insert(1)
s.removeMin()
s.insert(1)
s.removeMin()
s.removeMin()
s.removeMin()
s.insert(2)
s.insert(1)
s.removeMin()