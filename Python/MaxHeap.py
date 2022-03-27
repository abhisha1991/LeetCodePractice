class Solution():
    def __init__(self):
        # note we always always start with index 1 in heap
        # this allows us to get left/right children easily
        # based on formula - left = 2i, right = 2i + 1
        self.heap = ['#']
        self.size = 0
        
    def swap(self, i, j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp

    def print(self):
        print("Heap so far is...")
        for i in range(1, self.size+1):
            print(self.heap[i])

    def leftChild(self, parent):
        return 2 * parent
    
    def rightChild(self, parent):
        return 2 * parent + 1
    
    def parent(self, child):
        return int(child/2)

    def peekMax(self):
        return self.heap[1]
    
    def removeMax(self):
        if self.size == 0:
            print("Heap is empty, no max element to remove")
            return None
        
        maxEle = self.peekMax()
        print(f"Removing max element: {maxEle}")

        # swap 1st and last element
        self.swap(1, self.size)
        self.size -=1
        self.heap.pop()

        # remake into a heap
        self.heapify()
        self.print()

        return maxEle

    def insert(self, val):
        print(f"Inserting value: {val}")
        self.heap.append(val)
        self.size +=1
        self.heapify()
        self.print()
    
    def heapify(self):
        if self.size == 0:
            return
        
        child = self.size
        while child > 1:
            parent = self.parent(child)
            left = self.leftChild(parent)
            right = self.rightChild(parent)

            if child != left and child != right:
                raise Error("something is wrong with obtaining child")

            # if there is no right element, which is possible (imagine inserting 2nd element in a brand new heap)
            # so just compare parent and left
            if right > self.size:
                if self.heap[parent] < self.heap[child]:
                    self.swap(parent, child)
                child = parent
                continue

            # if there is a right child
            # determine who is bigger of the 2 children, and make that as the child
            # needed so that we only compare parent with largest child (maxheap)
            if self.heap[left] > self.heap[right]:
                child = left
            else:
                child = right

            if self.heap[parent] < self.heap[child]:
                self.swap(parent, child)
            child = parent

s = Solution()
s.insert(4)
s.insert(4)
s.insert(8)
s.insert(9)
s.insert(19)
s.insert(119)
s.removeMax()
s.removeMax()
s.insert(10)
s.insert(100)
s.removeMax()
s.removeMax()
s.removeMax()
s.removeMax()
s.removeMax()
s.removeMax()
s.removeMax()
s.removeMax()
s.removeMax()
s.removeMax()
s.removeMax()

