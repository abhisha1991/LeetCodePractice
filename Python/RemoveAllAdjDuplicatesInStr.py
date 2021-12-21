# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/submissions/
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for i in S:
            if not stack:
                stack.append(i)
                continue
            if i == stack[-1]:
                stack.pop()
                continue
            stack.append(i)
            
        return "".join(stack)