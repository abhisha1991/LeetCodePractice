# https://leetcode.com/problems/insert-delete-getrandom-o1
import random
class RandomizedSet:

    def __init__(self):
        self.dic = dict()

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            self.dic[val] = None
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dic:
            del self.dic[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.dic.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()