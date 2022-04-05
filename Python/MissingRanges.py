# https://leetcode.com/problems/missing-ranges
# this is o(n) memory solution, which gets memory exceeded in LC
# however, this does work if there were no memory constraints
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        i = lower
        
        def format(l, u):  
            if l > u:
                return None
            
            if l == u:
                return str(l)
                
            return str(l) + "->" + str(u)
        
        if nums == []:
            return [format(lower, upper)]
        
        if len(nums) == 1:
            if nums[0] == lower:
                if format(lower+1, upper) == None:
                    return []
                return [format(lower+1, upper)]
                    
            if nums[0] == upper:
                if format(lower, upper-1) == None:
                    return []
                else:
                    return [format(lower, upper-1)]
                
            return [format(lower, nums[0]-1), format(nums[0]+1, upper)]
        
        res = []
        missing = []
        # now nums has at least 2 elements
        # form an arr of missing nums
        j = 0
        while i <= upper and j < len(nums):
            cur = nums[j]
            while i < cur:
                missing.append(i)
                i +=1
                
            j +=1
            i +=1
        
        # add remaining missing elements from nums[-1] to curr
        while i <= upper:
            missing.append(i)
            i +=1
            
        print(missing)
        if missing == []:
            return  []
        
        # now convert missing nums to ranges
        i = 0
        j = 1
        while j < len(missing):
            if missing[j] != missing[i]+1:
                # single number range found
                res.append(format(missing[i], missing[i]))
                i +=1
                j +=1
                continue
                
            low = missing[i]
            high = missing[i]
            while j < len(missing) and missing[i]+1 == missing[j]:
                high = missing[j]
                i +=1
                j +=1
            res.append(format(low, high))
            i = j
            j += 1
        
        # now j is out of bounds
        # there still may be a single element left in ith position
        # consider example lower = 0, upper = 9 and arr is [5,8]
        # missing is [0, 1, 2, 3, 4, 6, 7, 9]
        # so far, with this algo, we get res as ["0->4","6->7"]
        # we are expecting res to be ["0->4","6->7", "9"]
        if res:
            last = res[-1]
        else:
            last = ''
            
        i = missing[-1]
        if str(i) not in last:
            res.append(format(i, i))
        
        return res