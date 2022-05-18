class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False
        
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        # holds remainder of prefix sum as key
        # value is last seen index where this remainder occurred
        dic = dict()
        
        # to handle if nums[0] is itself divisible by k
        dic[0] = -1
        
        for i in range(len(prefix)):
            r = prefix[i] % k
            if r not in dic:
                dic[r] = i
            # length of the arr, ie, diff of indices must be 2 or more
            elif i - dic[r] > 1:
                return True
        return False