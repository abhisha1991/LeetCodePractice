# https://leetcode.com/problems/jump-game/description/
# https://www.youtube.com/watch?v=jH_5ypQggWg

from os import sys
class Solution(object):
    # solution also available in section 5.4 in EPI
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        The basic idea is this: at each step, we keep track of the furthest reachable index. 
        The nature of the problem (eg. maximal jumps where you can hit a range of targets instead of singular 
        jumps where you can only hit one target) is that for an index to be reachable, each of the previous indices 
        have to be reachable.

        Hence, it suffices that we iterate over each index, 
        and If we ever encounter an index that is not reachable, 
        we abort and return false. By the end, we will have iterated to the last index. 
        If the loop finishes, then the last index is reachable.
        '''
        maxJump = 0
        maxIdx = len(nums) - 1
        for i in range(len(nums)):
            # if the furthest we can advance is not good enough, ie to reach "i", let alone end of array, then return false
            if maxJump < i:
                return False
            # the furthest we can advance from index i is i + nums[i]
            maxJump = max([maxJump, i + nums[i]])
        return True

        # return self.solve(nums, 0, 0)
        # return self.minJumpFunc(nums)

    # this should also work, but is a worse solution as it uses stack space
    def solve(self, nums, idx, mj):
        # the furthest we can go given that we are at index idx is idx + nums[idx]
        # if we cannot even reach the current idx, we wont be able to move ahead
        if mj < idx:
            return False
        if idx < len(nums) - 1:
            return self.solve(nums, idx+1, max(mj, idx + nums[idx]))
        return True

    # like Longest Inc subsequence problem, this is also o(n2) so its exceeding the time limit
    def minJumpFunc(self, nums):
        minjump = [sys.maxsize] * len(nums)
        jumpfrom = [None] * len(nums)
        minjump[0] = 0
        jumpfrom[0] = 0
        for i in range(1, len(nums)):
            j = 0
            while j < i:
                if j + nums[j] >= i:  # if you can reach index i from j
                    # print("index i can be reached from j", i, j)
                    temp = min([minjump[i], 1 + minjump[j]])
                    if temp < minjump[i]:
                        minjump[i] = temp
                        jumpfrom[i] = j
                j += 1

        # print("minjump is", minjump)
        # print("jumpfrom is", jumpfrom)
        if minjump[-1] != sys.maxsize:
            return True
        return False


