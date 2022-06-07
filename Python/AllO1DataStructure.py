# https://leetcode.com/problems/all-oone-data-structure
from collections import defaultdict
import random
class Bucket:
    def __init__(self, freq):
        self.freq = freq
        self.vals = set()
        self.nxt = None
        self.prev = None
    
    def add(self, val):
        self.vals.add(val)
    
    def remove(self, val):
        self.vals.remove(val)
    
    def get(self):
        if self.vals:
            return random.choice(list(self.vals))
        return ""
    
    def isempty(self):
        if not self.vals:
            return True
        return False
    
    def deleteNode(self, node):
        prev = node.prev
        nxt = node.nxt
                
        prev.nxt = nxt
        nxt.prev = prev
                
        node.prev = None
        node.nxt = None
    
    def insertNode(self, prev, nxt, node):
        prev.nxt = node
        node.prev = prev
        node.nxt = nxt
        nxt.prev = node
        
class AllOne:

    def __init__(self):
        self.key2freq = defaultdict(int)
        self.freq2bucket = dict()
        self.head = Bucket(-1)
        self.tail = Bucket(-1)
        
        # create double linked list pointing head and tail to each other
        self.head.nxt = self.tail
        self.tail.prev = self.head
        
        self.head.prev = self.tail
        self.tail.nxt = self.head
    
    # pattern for increment is to add key to new freq bucket, and remove from old freq bucket
    def inc(self, key: str) -> None:
        prevF = self.key2freq[key]
        self.key2freq[key] +=1
        newF = self.key2freq[key]
        
        # when prevF is 0, and newF is 1
        if prevF not in self.freq2bucket and newF not in self.freq2bucket:
            b = Bucket(newF)
            self.freq2bucket[newF] = b
            b.freq = newF
            b.add(key)
            
            # maintain in double linked list
            # insert b between self.head and nxt
            nxt = self.head.nxt
            self.head.insertNode(self.head, nxt, b)
            return
        
        elif prevF not in self.freq2bucket and newF in self.freq2bucket:
            newb = self.freq2bucket[newF]
            newb.add(key)
            return
        
        # for all below cases, prevF is in freq2bucket, so we want to increment key in newF bucket
        # and then decrement key from prevF bucket
        
        # when we increment a single key multiple times
        if newF not in self.freq2bucket:
            # add new freq bucket
            b = Bucket(newF)
            self.freq2bucket[newF] = b
            b.freq = newF
            b.add(key)
            
            # insert b between prevb and prevb.nxt
            prevb = self.freq2bucket[prevF]
            nxt = prevb.nxt
            
            self.head.insertNode(prevb, nxt, b)

        
        # when multiple keys are at play, some are with older freq. some with newer
        else:
            newb = self.freq2bucket[newF]
            newb.add(key)
            
        # we have added key in new frequency bucket, now its time to remove key from old freq bucket
        prevb = self.freq2bucket[prevF]
        prevb.remove(key)
        if prevb.isempty():

            # remove prevb from the linked list
            self.head.deleteNode(prevb)
            # delete from freq2bucket dictionary
            del self.freq2bucket[prevF]
        
        # print()
        # print(f"performed increment for key: {key}, going to print LL")
        # self.printLL()
    
    # pattern for dec is to add key to new freq bucket and remove from old freq bucket
    def dec(self, key: str) -> None:
        # key is guaranteed to exist per question
        prevF = self.key2freq[key]
        self.key2freq[key] -=1
        newF = self.key2freq[key]
        if prevF not in self.freq2bucket:
             raise Exception("dec: bucket doesn't exist for prevF")
        
        # special case - when new decremented freq is 0, we don't create a bucket for this new freq
        if newF == 0:
            del self.key2freq[key]
            
            # decrement key from previous freq bucket
            prevb = self.freq2bucket[prevF]
            prevb.remove(key)
            
            if prevb.isempty():
                # remove prevb from the linked list
                self.head.deleteNode(prevb)
                # delete from freq2bucket dictionary
                del self.freq2bucket[prevF]
            
            return
        
        # add key to corresponding frequency bucket
        if newF not in self.freq2bucket:
            # add new freq bucket
            b = Bucket(newF)
            self.freq2bucket[newF] = b
            b.freq = newF
            b.add(key)
            
            # insert b between prevb and prevb.nxt
            prevb = self.freq2bucket[prevF].prev
            nxt = prevb.nxt
            self.head.insertNode(prevb, nxt, b)
            
        else:
            newb = self.freq2bucket[newF]
            newb.add(key)
            
        # remove key from previous frequency bucket
        prevb = self.freq2bucket[prevF]
        prevb.remove(key)
        if prevb.isempty():
            # remove prevb from the linked list
            self.head.deleteNode(prevb)
            # delete from freq2bucket dictionary
            del self.freq2bucket[prevF]
        
        # print()
        # print(f"performed decrement for key: {key}, going to print LL")
        # self.printLL()
        
    def getMaxKey(self) -> str:
        # print("entering get max key, printing LL")
        # self.printLL()
        node = self.tail.prev
        if node == self.head:
            return ""
        
        return node.get()

    def getMinKey(self) -> str:
        # print("entering get min key, printing LL")
        # self.printLL()
        node = self.head.nxt
        if node == self.tail:
            return ""
        
        return node.get()
    
    def printLL(self):
        node = self.head
        while node.nxt != self.head:
            print(f"node with freq: {node.freq} and vals: {node.vals}")
            node = node.nxt
        # print tail explicitly
        print(f"node with freq: {node.freq} and vals: {node.vals}")
        
        
# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()