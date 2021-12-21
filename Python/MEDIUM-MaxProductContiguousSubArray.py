# https://leetcode.com/problems/maximum-product-subarray/discuss/
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # make res as nums[0], first number is potential result
        res = nums[0]
        # maxi and mini store the max and min prod uptill element nums[i]
        maxi = mini = res

        # start from index 1 till the end
        for i in range(1, len(nums)):
            # if the number itself was negative, then maxi and mini will change signs when multiplied to this number
            # example, (both +ve) if maxi = 5, mini = 3 and nums[i] -2 then maxi = -10, mini = -6, so we must swap to get correct maximum
            # example, (both -ve) if maxi = -3 and mini = -5, and nums[i] is -2, then maxi = 6, mini = 10, so we need to swap again
            # example, (1 +ve, 1 -ve) if maxi = 5, mini =-3, nums[i] is -2, then maxi = -10, mini = 6, so we need to swap
            if nums[i] < 0:
                temp = maxi
                maxi = mini
                mini = temp

            # regardless of whether nums[i] is negative or not, you try to find the max product between maxi * nums[i] and nums[i] itself
            # a case where you will choose nums[i] over maxi * nums[i], is when nums[i] is +ve and maxi is -ve
            maxi = max([maxi * nums[i], nums[i]])
            mini = min([mini * nums[i], nums[i]])
            res = max([maxi, res])

        return res

