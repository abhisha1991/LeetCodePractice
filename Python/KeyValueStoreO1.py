# Design a key value store which can perform all the following operations in Θ(1): (amortized) time complexity:
# V get(K)
# (K,V) getRandom()
# void put(K, V)
# V delete(K)

import random
class Solution():
    def __init__(self):
        self.dic = dict()
        self.arr = []

        # idx of last pos of the array
        # this is to avoid len(arr) which will be o(n) operation during put
        self.count = 0
        
    def get(self, key):
        if key not in self.dic:
            return None
            
        return self.dic[key][0]
    
    def put(self, key, value):
        if key not in self.dic:
            self.dic[key] = (value, self.count)
            # increment the last counter 
            self.count +=1
            self.arr.append(key)
            return
            
        pos = self.dic[key][1]
        self.dic[key] = (value, pos)    
    
    def getRandom(self):
        if not self.arr:
            return None
            
        key = random.choice(self.arr)
        return (key, self.dic[key][0])
    
    def delete(self, key):
        if key not in self.dic:
            return
        
        pos = self.dic[key][1]
        last = self.count - 1
        
        # swap pos and last
        tmp = self.arr[pos]
        self.arr[pos] = self.arr[last]
        self.arr[last] = tmp
        
        # decrement last array pos by 1
        self.count -=1
        # if last pos, ie, count underflows to negative, then reset to 0
        if self.count < 0:
            self.count = 0
        
        # the item that was earlier 'last' and now is at 'pos' after the swap
        # we need to update its position
        k = self.arr[pos]
        v = self.dic[k][0]
        self.dic[k] = (v, pos)
        
        # delete the item 'key' both from array and from dictionary
        self.arr.pop()
        del self.dic[key]


s = Solution()
# put in fresh keys 'a' and 'b'
s.put('a', 1)
s.put('b', 2)
print(s.dic)
print(s.arr)

# get values
print(s.get('a'))
print(s.get('b'))

# get random values
print(s.getRandom())
print(s.getRandom())
print(s.getRandom())

# delete 1 key
s.delete('a')
print(s.dic)
print(s.arr)

# delete last key
s.delete('b')
print(s.dic)
print(s.arr)

# add to empty KV store
# with overriding 'b' value
s.put('a', 1)
s.put('b', 2)
s.put('b', 3)

print(s.dic)
print(s.arr)

s.delete('b')
print(s.dic)
print(s.arr)

# delete an already deleted key
s.delete('b')
print(s.dic)
print(s.arr)

# delete last key
s.delete('a')
print(s.dic)
print(s.arr)

# add to empty KV store
# with 3 keys
s.put('a', 1)
s.put('b', 2)
s.put('c', 3)

print(s.dic)
print(s.arr)

# delete random key
s.delete('b')
print(s.dic)
print(s.arr)

# get random values
print(s.getRandom())
print(s.getRandom())

# delete already deleted key and other keys
s.delete('a')
s.delete('b')
s.delete('c')

# get random values from empty KV store
print(s.getRandom())
print(s.getRandom())