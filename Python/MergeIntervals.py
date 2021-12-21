# https://leetcode.com/problems/merge-intervals/submissions/
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort intervals by first key
        intervals.sort()
        if len(intervals) == 0:
            return []
        stack = []
        # add first interval
        stack.append(intervals[0])
        # skip 0th interval as we have already added it, so we start with 1
        # consider (a,b) which is top of stack
        # consider (c,d) which is the curr element
        # note that a <= b - why? because (a,b) is start and end of interval
        # note that a <= c, why? because we have sorted intervals in the beginning
        # case: a <= c <= b --> merge --> [a, max(b,d)]
        # case: a <= b < c --> dont merge
        # case: a <= d <= b --> note a <=c, this means (a,b) captures the entire segment, so no need for (c,d)
        for i in range(1, len(intervals)):
            curr = intervals[i]
            st = stack[-1]
            if (curr[0] >= st[0] and curr[0] <= st[1]):
                end = max(st[1], curr[1])
                stack.pop()
                stack.append([st[0], end])
            elif curr[0] > st[1]:
                stack.append(curr)
                    
                    
        return stack