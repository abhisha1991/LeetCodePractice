# https://leetcode.com/problems/sliding-window-maximum/description/
# https://www.youtube.com/watch?v=J6o_Wz-UGvc&t=84s
'''
For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].
'''
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        # dq will contain the indexes of a queue such that it has strictly decreasing elements of the window in consideration
        dq = []
        i = 0
        while i < len(nums):

            # if we are going out of the window, remove the first element of the dq
            if (len(dq) > 0 and dq[0] == i - k):
                dq = dq[1:]

            # we're maintaining a strictly decreasing queue in dq,
            # so if the back of the queue is smaller than the current number being inserted, remove them from dq
            while (len(dq) > 0 and nums[dq[len(dq) - 1]] < nums[i]):
                dq = dq[0:len(dq) - 1]

            # add current element index of the window
            dq.append(i)
            # if the current index > first k elements, then insert first index of the dq as that will be largest element in the window
            if i >= k - 1:
                res.append(nums[dq[0]])
            i += 1
        return res