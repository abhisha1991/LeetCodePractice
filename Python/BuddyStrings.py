# https://leetcode.com/problems/buddy-strings/
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        # handle cases like 'aa', vs 'aa'
        # or 'abab' vs 'abab'
        if s == goal and len(set(s)) < len(s):
            return True
        
        # find the place where the indices actually differ
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        
        if len(diff) > 2:
            return False
        
        # len of diff is 2, which has the 2 indices where the strings differed
        # this inner if is the key part, diff has 2 indices, say [0, 10]
        # now it must be the case that s[0] == goal[10] and vice versa for the swap to work
        if len(diff) == 2:
            if s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]:
                return True

        return False