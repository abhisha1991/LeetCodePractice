# asked in Amazon Ec2 interview (2018) and Google: 
# https://leetcode.com/discuss/interview-question/619524/Google-or-Onsite-or-Random-Generator
# generate a random number between 0 and n (inclusive)
# n is passed into constructor
# never return a number that you have already returned, if you run out of options, return -1
import random
class Solution():
    def __init__(self, n):
        self.n = n
        self.start = 0
        self.arr = [i for i in range(n+1)]

    def generate(self):
        if self.start > self.n:
            return -1
        
        # get random index from start to n
        # get a random integer in the range [a, b] including both end points.
        idx = random.randint(self.start, self.n)
        out = self.arr[idx]

        # get element at start and store in tmp
        tmp = self.arr[self.start]
        # replace element at start with out var
        self.arr[self.start] = out
        # store what was in start into later part of array
        self.arr[idx] = tmp

        # increment start so everything from 0 to start-1 inclusive is "reserved"
        # and is forbidden from being returned next time
        self.start +=1
        
        return out

# test 1
s = Solution(10)
res = []
for i in range(11):
    res.append(s.generate())

print(res)

# test 2
res = []
s = Solution(10)
for i in range(15):
    res.append(s.generate())

print(res)