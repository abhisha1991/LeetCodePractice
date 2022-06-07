# https://leetcode.com/problems/find-the-celebrity
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # consider 3 people A, B, C
        # for A to be a celeb, everyone must know A, but A must know no one
        # ie, indegree on A should be 2, ie, n-1, and outdegree must be 0
        
        # if A --> B (ie, A knows B returns true)
        # we know for sure A cannot be a celeb, so we can rule out A
        # since celebs are not allowed to know anyone, ie, outdegree == 0
        
        # if A --> B (ie, A knows B returns false)
        # then we know that B cannot be a celeb, since everyone must know the celeb (indegree == n-1)
        
        # make everyone a celeb, and then we'll use above strategy to discard them
        celebs = set()
        for i in range(n):
            celebs.add(i)
        
        # initial celeb count
        count = len(celebs)
        
        while True:
            while len(celebs) > 2:
                c = list(celebs)
                i = c[0]
                j = c[1]
                
                # for every knows call, we either discard i or j
                # explanation for this is above
                if knows(i, j):
                    celebs.discard(i)
                else:
                    celebs.discard(j)
            
            # if our count of celebs is not changing anymore, then break
            if count == len(celebs):
                break
            
            # re-count the number of celebs after discarding a bunch of them
            count = len(celebs)
        
        
        def isCeleb(c):
            # if i does not know c, then 'c' cannot be a celeb
            for i in range(n):
                if c != i and not knows(i, c):
                    return False

            # if c knows i, then 'c' cannot be a celeb
            for i in range(n):
                if c != i and knows(c, i):
                    return False
            
            return True
        
        # go through list of pruned celebs
        for c in list(celebs):
            if isCeleb(c):
                return c
            
        return -1