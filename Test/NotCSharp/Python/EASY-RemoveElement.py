# https://leetcode.com/problems/remove-element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        length = len(nums)
        j = length - 1
        if length == 0:
            return 0
        
        while i < j:
            if nums[i] == val and nums[j] != val:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                
                i +=1
                j -=1
            else:
                if nums[i] != val:
                    i +=1
                if nums[j] == val:
                    j -=1
    
        for i in range(0, length):
            if nums[i] == val:
                if i == 0:
                    return 0
                else:
                    return i