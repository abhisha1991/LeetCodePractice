# https://leetcode.com/problems/sliding-window-maximum/description/
# https://www.youtube.com/watch?v=DfljaUwZsOk
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
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        i = 0
        output = []
        
        # if there are fewer than k elements in nums
        # directly return max
        if len(nums) <= k:
            return [max(nums)]
        
        # BRUTE FORCE 
        # go through k elements at a time, find max of k elements
        # add to output as you go along. Time complexity is o(n-k)*o(k)
        
        # OPTIMIZED
        # use a double ended q (dequeue) -- allows for removal/addition at both ends in o(1)
        # in python, this is just a regular queue
        # there are 2 things we want to happen in this queue so we get our results easily
        # 1. only keep current window k elements in queue, eject older elements (allows us to be sure we're only looking in the window!)
        # 2. q is in decreasing order, so front of q is largest element at any instant (allows us to get the max of the window by looking at q[0])
        
        # time complexity is o(n)
        # note we store indices in q, not the elements themselves
        # why? its easier to eject older elements this way
        for i in range(0, len(nums)):
            # if the front of the q (index) has gone out of bounds of the window
            # then remove from front of q, 
            # we want to keep only "current window" elements in q
            if q and i-q[0] >= k:
                q.pop(0)
            
            # start popping from the right if current element is 
            # larger than the right most element of q
            # ultimately we want a situation where front of q contains largest
            # element of the current window
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            
            # add current element
            q.append(i)
            
            # after k-1 index, we have a q of size k always for every element i
            # so we want to start adding to output as we go along
            if i >= k-1:
                # remember, in this q, since we constrained it to be decreasing
                # front of q will be largest always
                output.append(nums[q[0]])
                
        return output        
        