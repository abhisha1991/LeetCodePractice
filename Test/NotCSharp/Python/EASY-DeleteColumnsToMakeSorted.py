#https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        for i in zip(*A):
            if list(i) != sorted(list(i)):
                count+=1
        return count
