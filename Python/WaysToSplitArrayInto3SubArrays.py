# https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/
import bisect
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [0]
        for x in nums: 
            prefix.append(prefix[-1] + x)
        
        mod = 10**9 + 7
        ans = 0
        for i in range(1, len(nums)): 
            j = bisect_left(prefix, 2*prefix[i])
            k = bisect_right(prefix, (prefix[i] + prefix[-1])//2)
            ans += max(0, min(len(nums), k) - max(i+1, j))
        return ans % mod
    
    def waysToSplit2(self, nums: List[int]) -> int:
        prefix = [0]
        # note that while nums is not in increasing order
        # but since nums only consists of positive numbers, prefix sum will be in increasing order
        for x in nums:
            prefix.append(prefix[-1] + x)
        
        # prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j]
        # consider lhs of the equation
        # prefix[i] <= prefix[j] - prefix[i]
        # 2 * prefix[i] <= prefix[j]
        
        # now consider rhs of the equation
        # prefix[j] - prefix[i] <= prefix[-1] - prefix[j]
        # 2 * prefix[j] <= prefix[i] + prefix[-1]
        # prefix[j] <= (prefix[i] + prefix[-1])/2
        
        # this means that for the above condition to be true (lhs <= mid <= rhs)
        # these 2 conditions must be true - "prefix[j] <= (prefix[i] + prefix[-1])/2" and "2 * prefix[i] <= prefix[j]"  
        ways = 0
        j = 0
        mod = 10**9 + 7
        
        def binsearch_right(arr, target, low, high):
            if low > high:
                return -1
            
            mid = (low+high)//2
            if target == arr[mid]:
                return mid
            
            if mid > 0 and arr[mid] >= target and arr[mid-1] < target:
                return mid
            
            if arr[mid] < target:
                return binsearch_right(arr, target, mid+1, high)
            
            # arr[mid] is greater than target
            # we want to keep running binsearch until we are as close to the right of target
            return binsearch_right(arr, target, low, mid-1)
        
        def binsearch_left(arr, target, low, high):
            if low > high:
                return -1
            
            mid = (low+high)//2
            if target == arr[mid]:
                return mid
            
            if mid < len(arr)-1 and arr[mid] <= target and arr[mid+1] > target:
                return mid
            
            if arr[mid] < target:
                return binsearch_left(arr, target, mid+1, high)
            
            # arr[mid] is greater than target
            # we want to keep running binsearch until we are as close to the left of target
            return binsearch_left(arr, target, low, mid-1)
        
            
        # let i be the ending index from index 0 -- this is what will be in the left part
        # then we need to find j,k via binary search on a sorted prefix sum array
        for i in range(1, len(prefix)):
            start = 0
            end = len(prefix)-1
            condition1 = 2 * prefix[i]
            condition2 = (prefix[i] + prefix[-1])/2
            # find index j whose element is just right or equal to "2 * prefix[i]"
            j = binsearch_right(prefix, condition1, start, end)
            # find index k whose element is just left or equal to "(prefix[i] + prefix[-1])/2"
            k = binsearch_left(prefix, condition2, start, end)
            
            if j != -1 and k != -1 and prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j]:
                ways += k-j+1
        
        return ways % mod