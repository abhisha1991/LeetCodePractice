# https://leetcode.com/problems/find-original-array-from-doubled-array
from collections import defaultdict
from collections import deque
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        
        # dictionary is going to hold a number and all its indexes in changed
        # its a default dict of deque, it can also be a list, but deque gives faster popleft perf
        dic = defaultdict(deque)
        
        # smallest number in changed (globally smallest), will also be smallest number in original array
        # so we want to take smallest number, say n, and see if 2n exists in dic
        changed.sort()
        
        for i in range(len(changed)):
            if changed[i] not in dic:
                dic[changed[i]] = deque([i])
            else:    
                dic[changed[i]].append(i)
        
        
        res = []
        for i in range(len(changed)):
            # get smallest
            smallest = changed[i]
            
            # if number is visited
            if smallest == '#':
                continue
            
            # get double
            double = 2 * smallest
            
            if not dic[smallest]:
                return []
            
            smIdx = dic[smallest].popleft()
            
            if not dic[double]:
                return []
            
            dbIdx = dic[double].popleft()
            
            # number and its double was found
            res.append(smallest)
            
            # mark smallest number and its double as visited
            changed[smIdx] = '#'
            changed[dbIdx] = '#'
        
        return res