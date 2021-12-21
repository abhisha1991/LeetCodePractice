# https://leetcode.com/problems/map-sum-pairs/description/
class MapSum(object):

    def __init__(self):
        self.d = {}

    def insert(self, key, val):
        self.d[key] = val

    def sum(self, prefix):
        return sum(self.d[i] for i in self.d if i.startswith(prefix))