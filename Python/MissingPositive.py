import sys
# https://leetcode.com/problems/first-missing-positive/description/
# https://www.youtube.com/watch?v=Dq0jQX3YNKg&t=458s - only works for positive numbers though (similar to this)
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        if len(nums) is 0:
            return 1

        n = sys.maxsize
        maxi = -sys.maxsize
        for i in range(len(nums)):
            # dic key = array element, value = frequency of element
            if nums[i] not in dic.keys():
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1

            # here we get n = smallest positive (>0) number in the array,
            # which should technically always be 1, else our answer is 1 (else condition) below
            if nums[i] > 0:
                if nums[i] < n:
                    n = nums[i]

            # maxi is largest element in array
            if nums[i] > maxi:
                maxi = nums[i]

        # if smallest positive number in array was 1, we can look forward till maxi to see which ele is missing from dic
        if n == 1:
            # can look forward till maxi
            for i in range(n, maxi):
                if i not in dic.keys():
                    return i
        else:
            return 1

        # a case like [0,1,2], where we return 3 or maxi + 1
        return maxi + 1