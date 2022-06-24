# https://leetcode.com/problems/random-pick-index
from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.count = 0
        self.dic = defaultdict(list)
        for i in range(len(nums)):
            self.dic[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.dic[target]) 

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)