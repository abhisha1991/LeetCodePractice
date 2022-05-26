# https://leetcode.com/problems/optimal-account-balancing
from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        persons = defaultdict(int)
        for fr, to, amt in transactions:
            persons[fr] += -amt
            persons[to] += amt 
        
        # notice we dont need persons whose balance is 0
        # they are already settled
        pos = [i for i in persons.values() if i > 0]
        neg = [i for i in persons.values() if i < 0]
        
        self.count = sys.maxsize
        
        def backtrack(positives, negatives, c):
            if len(positives) + len(negatives) == 0:
                self.count = min(self.count, c)
                return
            
            # get first negative
            n = negatives[0]
            
            # try to balance out this first negative with positives
            for p in positives:
                # there is a perfect match
                if p == -n:
                    remainPos = list(positives)
                    remainPos.remove(p)
                    
                    remainNeg = list(negatives)
                    remainNeg.remove(n)
                    
                    backtrack(remainPos, remainNeg, c+1)
                
                # example 100 against -40
                # we can eliminate -40 debt completely, but will be left with surplus of 60
                elif p > -n: 
                    r = p + n
                    
                    remainPos = list(positives)
                    remainPos.remove(p)
                    remainPos.append(r)
                    
                    remainNeg = list(negatives)
                    remainNeg.remove(n)
                    
                    backtrack(remainPos, remainNeg, c+1)
                
                # example 100 against -500
                # we can eliminate 100 from positives, but we will be left with a debt balance of -400
                else:
                    r = p + n
                    
                    remainPos = list(positives)
                    remainPos.remove(p)
                    
                    remainNeg = list(negatives)
                    remainNeg.remove(n)
                    remainNeg.append(r)
                    
                    backtrack(remainPos, remainNeg, c+1)
                    
        backtrack(pos, neg, 0)
        return self.count