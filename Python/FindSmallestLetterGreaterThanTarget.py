# https://leetcode.com/problems/find-smallest-letter-greater-than-target
import bisect
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        
        l = bisect.bisect_left(letters, target)
        r = bisect.bisect_right(letters, target)
        if l == r:
            return letters[l]
        
        if r == len(letters):
            return letters[0]
        return letters[r]