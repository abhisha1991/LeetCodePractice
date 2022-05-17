# https://leetcode.com/problems/group-shifted-strings/
from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        for s in strings:
            if len(s) == 1:
                dic[0].append(s)
                continue
            
            arr = []
            for i in range(1, len(s)):
                # regular case: consider acfg --> bdgh
                '''
                for acfg
                c-a = 2
                f-c = 3
                g-f = 1
                so arr is [2,3,1]
                
                for bdgh
                d-b = 2
                g-d = 3
                h-g = 1
                so arr is [2,3,1]
                
                because these are same arr "key", so these come under same group
                '''
                
                # special case: consider afg --> zef
                '''
                for afg
                f-a = 5
                g-f = 1
                so arr is [5,1]
                
                for zef
                z-e = 26-5 = 21
                f-e = 1
                so arr is [21,1]
                
                so they won't be grouped together, but they should
                so how do we convert 21 to 5? we take a mod of 26
                21 % 26 = 5
                arr becomes [5,1] for zef
                '''
                
                # special case: consder az --> ba
                '''
                z-a = 26-1 = 25 % 26 = 1
                b-a = 1-2 = -1 % 26 = -1
                
                this is why after taking mod, we do abs 
                '''
                x = ord(s[i]) - ord(s[i-1])
                x = abs(x % 26)
                arr.append(x)
            
            dic[tuple(arr)].append(s)
        
        res = []
        for v in dic.values():
            res.append(v)
        return res