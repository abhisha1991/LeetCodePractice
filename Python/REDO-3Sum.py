# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        nums.sort()
        for i in range(len(nums)):
            # here we are skipping duplicate elements
            # if i > 0, then we see current element and prev element, if they're same,
            # it means we've processed prev element so we dont need to process this one
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                target = nums[i] + nums[j] + nums[k]
                if target == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    # here we are skipping duplicate elements, we've processed j, so no need to do j+1
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    # here we are skipping duplicate elements, we've processed k, so no need to do k-1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                    j += 1
                elif target < 0:
                    j += 1
                else:
                    k -= 1

        return res

