#https://leetcode.com/problems/jewels-and-stones/submissions/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        from collections import Counter
        jewels = Counter(J)
        count = 0

        for i in list(S):
            if i in jewels.keys():
                count+=1
        return count
