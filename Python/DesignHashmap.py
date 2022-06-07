# https://leetcode.com/problems/design-hashmap/
# this is the cheating way of doing it, since we are creating an artificial capacity
class MyHashMap2:

    def __init__(self):
        self.cap = 10**5
        self.arr = ['#'] * self.cap

    def put(self, key: int, value: int) -> None:
        self.arr[key % self.cap] = value

    def get(self, key: int) -> int:
        v = self.arr[key % self.cap]
        return -1 if v == '#' else v
    
    def remove(self, key: int) -> None:
        self.arr[key % self.cap] = '#'

class MyHashMap:

    def __init__(self):
        self.prime = 2069 # can be any large prime number
        self.arr = [[] for i in range(self.prime)]

    def put(self, key: int, value: int) -> None:
        pos = key % self.prime
        self.remove(key)
        self.arr[pos].append((key, value))

    def get(self, key: int) -> int:
        pos = key % self.prime
        if not self.arr[pos]:
            return -1
        
        for k,v in self.arr[pos]:
            if k == key:
                return v
            
        return -1
    
    def remove(self, key: int) -> None:
        pos = key % self.prime
        if not self.arr[pos]:
            return
        
        self.arr[pos] = [(kv[0], kv[1]) for kv in self.arr[pos] if kv[0] != key]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)