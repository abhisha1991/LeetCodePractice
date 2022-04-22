# https://leetcode.com/problems/minimum-increment-to-make-array-unique
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        prev = nums[0]
        
        # notice that the loop starts from 1
        # say your input is [3,2,1,2,1,7,7]
        # sorted input becomes [1,1,2,2,3,7,7]
        '''
        prev = 1 (nums[0])
        cur = 1  (nums[1])
        
        now prev >= cur (since 1==1)
        so we need 1 step to change the cur '1' to a '2' (prev-cur+1)
        we also indicate that cur now becomes '2' (prev+1)
        
        now prev = 2
        cur = 2 (nums[2])
        
        again prev >= cur (since 2==2)
        so we need 1 step to change the cur '2' to a '3' (prev-cur+1)
        we also indicate that cur now becomes '3' (prev+1)
        
        now prev = 3
        cur = 2 (nums[3])
        
        again prev >= cur (since 3>2)
        so we need 2 steps now to change the cur '2' to a '4' (prev-cur+1)
        we also indicate that cur now becomes '4' (prev+1)
        
        now prev = 4
        cur = 3 (nums[4])
        
        again prev >= cur (since 4>3)
        so we need 2 steps now to change the cur '3' to a '5' (prev-cur+1)
        we also indicate that cur now becomes '5' (prev+1)
        
        now prev = 5
        cur = 7 (nums[5])
        
        now prev < cur, so we don't do anything
        now prev = 7
        cur = 7 (nums[6])
        
        again prev >= cur (since 7==7)
        so we need 1 step now to change the cur '7' to a '8' (prev-cur+1)
        we also indicate that cur now becomes '8' (prev+1)
        
        now prev = 8
        and we exit
        '''
        for i in range(1, len(nums)):
            cur = nums[i]
            if prev >= cur:
                ans += prev - cur + 1
                cur = prev + 1
                
            prev = cur
        
        return ans
    
    # TLE
    def minIncrementForUnique2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        dic = dict()
        # min number of changes
        ans = 0
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = True
            else:
                # collision happened
                # so until there is collision, we keep incrementing this number
                while nums[i] + 1 in dic:
                    nums[i] +=1
                    ans +=1
                
                # finally no more collisions for nums[i]+1, so add this to dictionary
                dic[nums[i] + 1] = True
                ans +=1
                
        return ans