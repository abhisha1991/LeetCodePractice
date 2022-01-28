# https://leetcode.com/problems/valid-anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            if i in dic.keys():
                dic[i] +=1
            else:
                dic[i] = 1
        
        for i in t:
            if i not in dic.keys():
                return False
            else:
                dic[i] -=1
            
        for k,v in dic.items():
            if v != 0:
                return False
        
        return True