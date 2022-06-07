# https://leetcode.com/problems/design-bounded-blocking-queue/
from threading import Lock
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.q = collections.deque()
        self.enq = Lock()
        self.deq = Lock()
        self.capacity = capacity
        
        # when q is empty, no one should be able to dequeue
        # so acquire a deq lock
        self.deq.acquire()
    
    def changeLocks(self):
        # if there is still capacity left to add, then release lock so other producers can add to q
        if self.size() < self.capacity and self.enq.locked():
            self.enq.release()
            
        # allow for dequeing if the size > 0
        if self.size() > 0 and self.deq.locked():
            self.deq.release()
            
    def enqueue(self, element: int) -> None:
        self.enq.acquire()
        self.q.append(element)
        
        self.changeLocks()
        
    def dequeue(self) -> int:
        self.deq.acquire()
        output = self.q.popleft()
        
        self.changeLocks()
        return output

    def size(self) -> int:
        return len(self.q)