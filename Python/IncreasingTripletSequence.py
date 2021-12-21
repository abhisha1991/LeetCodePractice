# https://leetcode.com/problems/increasing-triplet-subsequence/discuss/
import sys
# best simple solution ever!
def increasingTriplet(self, nums):
        firstmin = sys.maxsize
        secondmin = sys.maxsize

        for i in nums:
            if i < firstmin:
                firstmin = i
            elif i < secondmin:
                if i == firstmin:
                    continue
                secondmin = i
            elif i > secondmin:
                return True
        return False

class Solution:
    # follows along the longest increasing sub sequence method
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lis = [1] * len(nums)
        j = 0
        i = 1
        flag = False
        while i < len(nums):

            if nums[j] < nums[i]:
                lis[i] = max(1 + lis[j], lis[i])
                if lis[i] == 3:
                    flag = True
                    break

            j += 1
            if j == i:
                j = 0
                i += 1

        print(lis)
        return flag
