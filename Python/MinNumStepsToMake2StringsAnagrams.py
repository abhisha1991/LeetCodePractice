class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic = dict()
        # consider 2 strings
        # s = leet and t = meat
        for ss in s:
            if ss not in dic:
                dic[ss] = 1
            else:
                dic[ss] +=1
        
        # right now dic is {l: 1, e: 2, t: 1}
        for tt in t:
            if tt in dic:
                dic[tt] -= 1
            else:
                dic[tt] = -1
        
        # now dic is {l: 1, e: 1, t: 0, m: -1, a: -1}
        # this means that we decremented 1 'e' and 1 't' since they were there in 'meat'
        # so we can change an 'l' to an 'm' and an 'e' to an 'a' to make 'leet' an anagram of 'meat'
        # so just count the positive numbers
        count = 0
        for k,v in dic.items():
            if v > 0:
                count +=v
        return count