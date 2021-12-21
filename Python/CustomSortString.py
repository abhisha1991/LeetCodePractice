# https://leetcode.com/problems/custom-sort-string/
from collections import defaultdict

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # this holds the number of occurrences of all characters in T
        dictt = dict()
        for i in range(len(T)):
            if T[i] not in dictt.keys():
                dictt[T[i]] = 1
            else:
                dictt[T[i]] += 1
        
        res =''
        for j in S:
            while j in dictt and dictt[j] > 0:
                res +=j
                dictt[j] -=1
            # remove the dictionary key once you have added all occurrences to res so you dont have to iterate on it again
            dictt.pop(j, None)
        
        # for the remaining keys that were in T and not in S, just add them to the end of res
        for k in dictt.keys():
            while dictt[k] > 0:
                res +=k
                dictt[k] -=1
        
        return res
        
        
        