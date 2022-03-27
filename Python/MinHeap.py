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