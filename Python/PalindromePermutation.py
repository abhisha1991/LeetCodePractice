# https://leetcode.com/problems/palindrome-permutation
from collections import defaultdict
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        self.dic = defaultdict(int)
        for i in s:
            self.dic[i] += 1
        
        countOdd = 0
        for v in self.dic.values():
            if v % 2 == 1:
                countOdd +=1
            
            if countOdd > 1:
                return False
        return True