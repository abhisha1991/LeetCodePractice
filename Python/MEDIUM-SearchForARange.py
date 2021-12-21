# https://leetcode.com/problems/search-for-a-range/description/

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binsearchleft(0, len(nums) - 1, nums, target)
        right = self.binsearchright(0, len(nums) - 1, nums, target)
        print("left", left)
        print("right", right)
        if left <= right:
            return [left, right]

        return [-1, -1]

    def binsearchleft(self, low, high, nums, target):
        print("entering bin search left")
        while low <= high:
            mid = int((low + high) / 2)
            print("mid is", mid)
            # this condition is different for left and right
            if nums[mid] < target:
                low = mid + 1
                print("low changed to", low)
            else:
                high = mid - 1
                print("high changed to", high)
        # we return low in the left case
        return low

    def binsearchright(self, low, high, nums, target):
        print("entering bin search right")
        while low <= high:
            mid = int((low + high) / 2)
            print("mid is", mid)
            # this condition is different for left and right
            if nums[mid] <= target:
                low = mid + 1
                print("low changed to", low)
            else:
                high = mid - 1
                print("high changed to", high)
        # we return high in the right case
        return high

s = Solution()
s.searchRange([5,7,7,8,8,10], 8)