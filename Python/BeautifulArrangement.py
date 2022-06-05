# https://leetcode.com/problems/beautiful-arrangement
class Solution:
    def countArrangement(self, n: int) -> int:
        # notice all x in nums is unique, this affects the permutations since we don't have to
        # worry about duplicate elements, thus we can use sets instead of arr
        nums = [x for x in range(1, n+1)]
        self.res = 0
        
        def permute(perm):
            if len(perm) == len(nums):
                self.res +=1
                return
            
            for i in range(len(nums)):
                if nums[i] not in perm:
                    # backtracking, ie, add nums[i] and remove after doing further permutations
                    perm.add(nums[i])
                    N = len(perm)
                    # check condition to permute further, else don't permute
                    # condition to permute further is that the element we just added -
                    # does that satisfy the beautiful arrangement (BA) condition? 
                    # if not, then no point continuing as the full permutation won't satisfy BA condition
                    
                    # the condition is the same as if we were using an arr
                    # and did arr.append(nums[i]), and then below did arr[-1] / N
                    if nums[i] % N == 0 or N % nums[i] == 0:
                        permute(perm)
                        
                    perm.remove(nums[i])
        
        # why make this a set - since o(1) lookup is needed (faster compared to arr) - see for loop inside permute function
        permute(set())
        return self.res