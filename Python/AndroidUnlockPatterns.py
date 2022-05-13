# https://leetcode.com/problems/android-unlock-patterns/
class Solution:
    def __init__(self):
        self.count = 0
        
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = dict()
        # if 1,3 is a skip edge, so is 3,1
        # this is capturing that 1,3 are connected via 2. 2 is center point
        skip[(1,3)] = 2
        skip[(3,1)] = 2
        
        skip[(1,7)] = 4
        skip[(7,1)] = 4
        
        # diagonals are allowed
        skip[(1,9)] = 5
        skip[(9,1)] = 5
        
        skip[(2,8)] = 5
        skip[(8,2)] = 5
        
        skip[(3,7)] = 5
        skip[(7,3)] = 5
        
        skip[(3,9)] = 6
        skip[(9,3)] = 6
        
        skip[(4,6)] = 5
        skip[(6,4)] = 5
        
        skip[(7,9)] = 8
        skip[(9,7)] = 8
        
        def backtrack(cur, visited):
            # length must be at least m to increase ans
            if len(visited) >= m:
                self.count +=1
            
            # can't have length be greater than n
            if len(visited) >= n:
                return
            
            # find next connector edge
            for nxt in range(1, 10):
                # not allowed to visit already visited edge from cur
                if nxt in visited:
                    continue
                
                # conditions for backtrack
                # 1. if edge is not in skip list (regular edge like 2,3) or
                # 2. if edge is a skip edge and its center value has been visited before
                
                # condition 2: say we are at (1,3), then skip[(1,3)] = 2
                # now 2 MUST have occurred before in our path for 1,3 to be connected
                # else we cant connect them (No jumps through the center non-selected dots are allowed)
                if (cur, nxt) not in skip or skip[(cur, nxt)] in visited:
                    # else take next and backtrack with it
                    # jump to nxt edge
                    visited.add(nxt)
                    backtrack(nxt, visited)
                    # remove nxt edge
                    visited.remove(nxt)
        
        # go through every element of key pad
        # with a fresh visited set
        for i in range(1, 10):
            v = set()
            v.add(i)
            backtrack(i, v) 
            
        return self.count