# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# https://www.youtube.com/watch?v=LPFhl65R7ww
import sys


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m is 0 and n is 0:
            return []
        if m is 0:
            return self.singleArrMedian(nums2)
        if n is 0:
            return self.singleArrMedian(nums1)

        if m <= n:
            x = nums1
            y = nums2
        else:
            x = nums2
            y = nums1
            # we have exchanged nums1 and nums2, so the lengths also have to be exchanged
            m = len(x)
            n = len(y)

        # x is smaller arr, y is larger. start,end are idx of x
        start = 0
        end = m
        while start <= end:
            partX = (start + end) / 2
            partY = (m + n + 1) / 2 - partX  # WHY +1 in m+n, that will forever remain a mystery
            leftX = self.emptyPartitionCheck(x[0:partX], False)
            leftY = self.emptyPartitionCheck(y[0:partY], False)
            rightX = self.emptyPartitionCheck(x[partX:], True)
            rightY = self.emptyPartitionCheck(y[partY:], True)
            maxLeftX = leftX[-1]
            maxLeftY = leftY[-1]
            minRightX = rightX[0]
            minRightY = rightY[0]
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # found
                return self.getMedian(m + n, maxLeftX, maxLeftY, minRightX, minRightY)
            elif maxLeftX > minRightY:
                end = partX - 1
            else:
                start = partX + 1

        raise Exception("code should not reach here, there is an error")

    def getMedian(self, l, maxLeftX, maxLeftY, minRightX, minRightY):
        if l % 2 == 1:
            return max(maxLeftX, maxLeftY)
        else:
            return float(max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2

    def emptyPartitionCheck(self, arr, inf):
        l = len(arr)
        if l == 0:
            if inf:
                # if inf return positive infinity, used for right side arrays
                return [sys.maxsize]
            else:
                # if not inf return negative infinity, used for left side arrays
                return [-sys.maxsize]
        return arr

    def singleArrMedian(self, arr):
        t = len(arr)
        if t % 2 == 1:
            return arr[int(t / 2)]
        else:
            idx = int(t / 2)
            return float(arr[idx] + arr[idx - 1]) / 2
