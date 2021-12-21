# https://leetcode.com/problems/lru-cache/description/
from collections import defaultdict
import time


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = defaultdict(list)
        self.cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print("Getting the value corresponding to key ", key)
        if len(self.cache) == 0:
            return -1

        for k, v in self.cache.items():
            if k == key:
                return self.cache[k][0]

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        print("Putting the foll key value {0} {1}".format(key, value))
        res = self.get(key)
        if res != -1:
            self.cache[key] = [value, time.time()]

        len_cache = len(self.cache)
        if len_cache < self.cap:
            self.cache[key] = [value, time.time()]
        else:
            kk = next(iter(self.cache))
            mintime = self.cache[kk][1]
            for k, v in self.cache.items():
                if v[1] < mintime:
                    mintime = v[1]
                    kk = k
            del self.cache[kk]
            self.cache[key] = [value, time.time()]

        print(self.cache)

# Your LRUCache object will be instantiated and called as such:

'''
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
'''
obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print("Getting value corresponding to key {0} -> {1}".format(1, obj.get(1)))
obj.put(3, 3)
print("Getting value corresponding to key {0} -> {1}".format(2, obj.get(2)))
obj.put(4, 4)
print("Getting value corresponding to key {0} -> {1}".format(1, obj.get(1)))
print("Getting value corresponding to key {0} -> {1}".format(3, obj.get(3)))
print("Getting value corresponding to key {0} -> {1}".format(4, obj.get(4)))
print(obj.cache)