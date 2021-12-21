# https://leetcode.com/problems/longest-consecutive-sequence/description/
# https://www.geeksforgeeks.org/longest-consecutive-subsequence/

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # having a set is important because look ups are o(1) - this is absolutely key
        s = set()
        for i in nums:
            s.add(i)

        res = 0
        for i in range(len(nums)):
            # we go through each element in nums, if element - 1 doesnt exist in set (o(1) lookup)
            # then it means that this element is a potential candidate to be the smallest element in the sequence
            # if there did exist a smaller element,
            # it means that nums[i] - 1 should be considered as the smallest potential element, not the current one
            if nums[i] - 1 not in s:
                # we have a potential smallest element
                j = nums[i]
                # count will store the number of elements in this sequence, it is a candidate for being max
                count = 0
                # again the look up is o(1), as long as we are increasing one unit and that element belongs to s
                # we should increase j and count
                while j in s:
                    j += 1
                    count += 1

                # res will be max of current value and new value coming in
                res = max([res, count])
        return res
