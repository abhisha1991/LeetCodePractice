# https://leetcode.com/problems/non-overlapping-intervals/submissions/
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) < 2:
            return 0
        
        intervals.sort(key=lambda x:x[1])
        result =  []
        # add first element
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            curr = intervals[i]
            # check if start of current element is more than end of last element in result
            # if it is, there is no overlap and it can be appended to result
            if curr[0] >= result[-1][1]:
                result.append(curr)
        print(result)
        return len(intervals) - len(result)