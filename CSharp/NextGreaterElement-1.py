# https://leetcode.com/problems/next-greater-element-i/submissions/
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums1)
        for idx1, n1 in enumerate(nums1):
            j = nums2.index(n1)
            while j < len(nums2):
                if n1 < nums2[j]:
                    res[idx1] = nums2[j]
                    break
                j +=1
                
        return res