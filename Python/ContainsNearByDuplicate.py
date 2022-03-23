# https://leetcode.com/problems/contains-duplicate-ii
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(list)
        
        for j in range(len(nums)):
            if nums[j] not in dic:
                dic[nums[j]].append(j)
            else:
                # the values in dic are sorted indices
                # as they're entered as a result of left to right parsing of nums
                # so we just need to get the last index and not iterate through all values of dic[nums[j]]
                i = dic[nums[j]][-1]
                if abs(i-j) <= k:
                    return True
                else:
                    dic[nums[j]].append(j)
        return False