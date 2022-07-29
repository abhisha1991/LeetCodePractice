# https://leetcode.com/problems/subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def sets(arr, start):
            ans.append(list(arr))
            for i in range(start, len(nums)):
                # populate arr from ground up
                arr.append(nums[i])
                
                # remember to recurse with i+1 not with start+1
                sets(arr, i+1)
                
                # nums elements are unique per question, so we're guaranteed to just remove the desired element
                # backtrack
                arr.remove(nums[i])
        
        
        sets([], 0)
        return ans