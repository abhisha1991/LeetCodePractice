# https://leetcode.com/problems/insert-delete-getrandom-o1
import random
from collections import defaultdict
class RandomizedSet:
    def __init__(self):
        self.dic = dict()
        self.arr = list()

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            # key in dict is the value we're inserting
            # value in dict is the index at which we're inserting this val in arr
            self.dic[val] = len(self.arr)
            
            # remember to add to both dict and arr
            self.arr.append(val)
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val in self.dic:
            idxEleToDel = self.dic[val]
            lastEle = self.arr[-1]
            idxLastEle = self.dic[lastEle]
            
            # swap elements - last element, and element to delete
            tmp = self.arr[idxEleToDel]
            self.arr[idxEleToDel] = self.arr[idxLastEle]
            self.arr[idxLastEle] = tmp
            
            # update index of lastEle
            # now last element which was NOT the one to delete
            # is sitting in the middle of the arr and has an updated idx (the one that belonged to index to delete)
            self.dic[lastEle] = idxEleToDel
            
            # clean up from list and dict
            # notice that deletion from list becomes o(1) now
            # since element to delete is the last one now (after swap)
            self.arr.pop()
            del self.dic[val]
            return True
        
        return False

    def getRandom(self) -> int:
        # list also contains the current values, so return one of them
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()