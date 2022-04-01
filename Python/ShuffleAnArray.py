# very similar to uniform random number generator
# except that we're generating the whole list at once
# https://github.com/abhisha1991/LeetCodePractice/blob/master/Python/RandomNumberGeneratorWORepeat.py
# https://leetcode.com/problems/shuffle-an-array/
class Solution:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.copy = [i for i in nums]

    def reset(self) -> List[int]:
        return self.copy

    def shuffle(self) -> List[int]:
        n = len(self.arr)
        for i in range(n):
            # pick another index between i and n-1
            # randint picks both sides inclusive, thus n-1
            idx = random.randint(i, n-1)
            
            # swap the 2 elements
            tmp = self.arr[idx]
            self.arr[idx] = self.arr[i]
            self.arr[i] = tmp
            
        return self.arr
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()