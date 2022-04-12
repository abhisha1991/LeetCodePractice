# https://leetcode.com/problems/random-pick-with-blacklist/
# https://www.youtube.com/watch?v=6QIbXSZ1s3Q
import random
class Solution:
    # this is o(b) time and space complexity
    def __init__(self, n: int, blacklist: List[int]):
        self.lenb = len(blacklist)
        self.N = n
        
        blset = set(blacklist)
        # temp is going to contain the list of whitelisted numbers
        # from N - lenb to N (ie, 2nd half of the array)
        # create set for o(1) lookup
        temp = set()
        # if lenb is small relative to N, then temp will be a small set
        # we hope the blacklist in general, is not a million numbers!
        for i in range(self.N - self.lenb, self.N):
            # in this range, there could be some numbers belonging to blacklist
            # don't add them to temp
            if i not in blset:
                temp.add(i)
        
        # bl2wl is a blacklist to whitelist mapping
        # it basically is storing a whitelist number in the "value" 
        # for every blacklist "key" it encounters in the 1st half (N - lenb) array.
        # strategy of mapping a whitelisted value for a blacklisted key is to be uniform
        # ie, store list_temp[i % len_temp] as value
        self.bl2wl = dict()
        list_temp = list(temp)
        len_temp = len(list_temp)
        
        for i in blacklist:
            if i < self.N - self.lenb:
                self.bl2wl[i] = list_temp[i % len_temp]
    
    def pick(self) -> int:
        # randint is inclusive on both sides, so we dont want upper to be N - lenb
        num = random.randint(0, self.N - self.lenb - 1)
        
        # return whitelist mapping for this blacklisted number if num was a blacklisted number
        if num in self.bl2wl:
            return self.bl2wl[num]
        
        # if num is not a blacklisted number, return as is
        return num

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()

'''
the obvious implementation of creating an explicit arr list without blacklist and using the standard implementation
results in a memory limit exceeded error

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.blist = set(blacklist)
        self.arr = [i for i in range(n) if i not in self.blist]
        self.ptr = 0
        self.N = len(self.arr)
        
    def pick(self) -> int:
        if self.ptr >= self.N:
            self.ptr = 0
        
        import random
        
        idx = random.randint(self.ptr, self.N-1)
        out = self.arr[idx]
        
        tmp = self.arr[self.ptr]
        self.arr[self.ptr] = out
        self.arr[idx] = tmp
        
        self.ptr +=1
        
        return out


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
'''