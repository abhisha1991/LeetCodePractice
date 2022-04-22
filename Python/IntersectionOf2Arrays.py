# https://leetcode.com/problems/intersection-of-two-arrays-ii
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = dict()
        dic2 = dict()
        for n in nums1:
            if n not in dic1:
                dic1[n] = 1
            else:
                dic1[n] +=1
        
        for n in nums2:
            if n not in dic2:
                dic2[n] = 1
            else:
                dic2[n] +=1
        
        ans = []
        for k,v in dic1.items():
            if k in dic2:
                # intersection means taking the min
                repeat = min(v, dic2[k])
                arr = [k] * repeat
                ans += arr
                
        return ans