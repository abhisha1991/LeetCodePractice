# https://leetcode.com/problems/intersection-of-two-arrays
from collections import defaultdict
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = defaultdict()
        len1 = len(nums1)
        len2 = len(nums2)
        
        for i in range(len1):
            if nums1[i] in dic:
                dic[nums1[i]][0] +=1
            else:
                dic[nums1[i]] = [1, 0]
        
        for i in range(len2):            
            if nums2[i] in dic:
                dic[nums2[i]][1] +=1
            else:
                dic[nums2[i]] = [0, 1]
        
        return [k for k,v in dic.items() if dic[k][0] >= 1 and dic[k][1] >= 1]
                
        