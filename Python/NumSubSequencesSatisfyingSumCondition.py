# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        '''
        https://www.youtube.com/watch?v=xCsIkPLS4Ls
        Consider sorted array 
        [3, 4, 6, 8] and target is 10
        
        Imagine if we decide we're picking the 3
        thus, we can form some subarrays such that their min val (3) + max val (TBD) <= target (10)
        
        Sub arrays of size 1, we can form:
        [3] --> min val = 3, max val = 3 (3+3 < 10)
        
        Sub arrays of size 2, we can form (remember we're def including the 3)
        [3,4]
        [3,6]
        
        Sub arrays of size 3, we can form:
        [3, 4, 6]
        
        So in effect, after choosing this 3, we can choose/not choose the other elements (2^x), 
        ie, number of sub arrays is going to be 2^(other elements to consider) => 2^(len([4,6])) = 2^2 = 4
        
        We can do this same exercise with element 4 and others
        we look only forward since we don't want to again include 3 (was already considered before)
        sub arrays will be [4], [4,6] or 2^(len([6])) = 2^1 = 2
        
        Question: how do we get the length of the subarrays to consider looking ahead? (example, len([4,6])) 
        Answer: we use a 2 pointer approach
        right points to largest element, left points to smallest element, the moment nums[left] + nums[right] <= target
        then the window size becomes right - left 
        '''
        mod = 10**9 + 7
        res = 0
        # sorting the array is fine because subsequences will still be formed, just not with the order preserved
        '''
        if array was actually, [6,4,8,3] and we sorted to [3,4,6,8]
        then with element 3, the sub arrays will still be [3], [3,4], [3,6], [3,4,6] but with diff order
        
        but sorting gives us the ability to use 2 pointer approach, thus we sort
        '''
        nums.sort()
        r = len(nums)-1
        
        l = 0
        while l <= r:
            # index left will be smallest element since arr is sorted
            # likewise, index right will contain largest element
            if nums[l] + nums[r] > target:
                r -=1
            else:
                # res += 2**(r - l) % mod
                res += pow(2, r - l, mod)
                l +=1
            
        return res % mod