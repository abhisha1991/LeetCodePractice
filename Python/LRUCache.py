# https://leetcode.com/problems/lru-cache/
from collections import OrderedDict
class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.nxt = None
        self.prev = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict() # key is key being inserted, value is node link address
        
        # least recent is in left.nxt
        # initialize these with dummy values
        self.left = Node(-1, -1)
        # most recent is in right.prev
        self.right = Node(-1, -1)
        
        # initially we want a connection between left and right
        self.left.nxt = self.right
        self.right.prev = self.left
    
    # removes node from double linked list
    def remove(self, node):
        l = node.prev
        r = node.nxt
        # get the node out of the way
        l.nxt = r
        r.prev = l
        
        node.prev = None
        node.nxt = None
        
    # inserts node between 'self.right' and 'ptr just to the left of self.right'
    def insert(self, node):
        # get the 'ptr' (tmp) to the left of self.right (ie, just to the left of our most recent dummy ptr) 
        # since we want to insert our given 'node' in between 'ptr' and 'self.right'
        tmp = self.right.prev
        
        # link the tmp to our node for it to become most recently used!
        tmp.nxt = node
        node.prev = tmp
        
        # link our node to be next to tmp
        node.nxt = self.right
        self.right.prev = node
    
    def printLL(self):
        print("printing linked list contents...")
        tmp = self.left
        while tmp != self.right.nxt:
            print(f"Key is {tmp.key}, value is {tmp.value}. IsCurNodeLeft: {tmp == self.left}. IsCurNodeRight: {tmp == self.right} ")
            tmp = tmp.nxt
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # cache[key] is the link address of the node
        val = self.cache[key].value
        
        # reposition this node to be most recently used
        self.remove(self.cache[key])
        self.insert(self.cache[key])

        # self.printLL()
        return val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update value
            node = self.cache[key]
            node.value = value
            # reposition this node to become most recently used in linked list
            self.remove(node)
            self.insert(node)
        else:
            # check if we have capacity to insert
            if len(self.cache) < self.cap:
                self.cache[key] = Node(key, value)
                self.insert(self.cache[key])
                
            else:
                # we need to evict least recently used
                # both from linked list and from cache
                # before we can insert our current key, value
                # least recently used is going to be next to self.left (on the right)
                lru = self.left.nxt
                kLru = lru.key
                # remove lru node from double linked list and from cache
                self.remove(lru)
                del self.cache[kLru]
                
                # now we can add this current key,value we were originally planning to add
                # note that capacity doesn't change here since we're already at capacity
                # and we just deleted an older key and added a newer one
                self.cache[key] = Node(key, value)
                self.insert(self.cache[key])
        
        # self.printLL()

# this is cheating of course, but in case you need a quick implementation, use this one
class LRUCache2:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.c = capacity
        assert(self.c > 0)
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        if len(self.cache.keys()) > self.c:
            self.cache.popitem(last = False)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)