# https://leetcode.com/problems/partition-to-k-equal-sum-subsets
from itertools import combinations
class Solution:
    # adds memoization, time complexity is k x 2^n
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        self.target = int(sum(nums)/k)
        
        used = [False] * len(nums)
        # memoization of states at any given time
        '''
        for example, consider a scenario in which:
        set1: elements at pos 0,1 - sum(set1) = target
        set2: elements at pos 2,3 - sum(set2) = target

        and using this, we have determined that we cannot form another set that will equal to self.target (say)
        then we can memoize this "selection state" - ie, "used" array can be memoized
        
        Thus if any other dfs tries to form a similar selection, ie, used = [T,T,T,T,F,F,...F], ie, set1 and set2 have been formed
        then we can immediately let that dfs call know that there won't be another set3 that can be formed, ie, cache(used) = False
        '''
        cache = dict()
        
        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            
            if tuple(used) in cache:
                return cache[tuple(used)]
            
            if subsetSum == self.target:
                cache[tuple(used)] = backtrack(0, k-1, 0)
                return cache[tuple(used)]
            
            if subsetSum > self.target:
                return False
            
            for j in range(i, len(nums)):    
                if used[j]:
                    continue
                
                used[j] = True
                
                if backtrack(j+1, k, subsetSum + nums[j]):
                    return True
                
                used[j] = False
            
            cache[tuple(used)] = False
            return cache[tuple(used)]
        
        return backtrack(0, k, 0)

    # we get a TLE for this since we are using combinations, which makes the solution factorial!
    # this is easier to understand, but less efficient
    def canPartitionKSubsets2(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        self.target = int(sum(nums)/k)
        self.soln = set()
        def backtrack(i, currSum, idxs):
            # if we get the current sum, then add the potential indexes that make up the target sum
            # into the soln set
            if currSum == self.target:
                self.soln.add(tuple(idxs))
                return
            
            # if we have exceeded the arr idx size or the target sum, then return
            if currSum > self.target or i >= len(nums):
                return
            
            # either include nums[i] in current sum and add 'i' idx to the list of indexes contributing to that target
            backtrack(i+1, currSum + nums[i], list(idxs) + [i])
            # or don't include nums[i] in current sum and don't add 'i' to the list of indexes contributing to target
            backtrack(i+1, currSum, list(idxs))
                    
        
        # this will be 2^n solution, where n is length of arr
        # because at every element, we are either including or not including the element in consideration
        backtrack(0, 0, [])    
        
        # now we will have a list of tuples, each of whom sums up to the target
        # the tuples contain the indexes that sum up to target
        
        # so what we need is to find a combination of k tuples, 
        # such that all of the k tuple's combined indexes make up the entire array
        '''
        example: [1,2,3,4,5,6,7,8] and k=3 means that we need to form 3 sets, each having a sum of 12
        
        the different ways how a sum of 12 is possible is as follows:
        {(0, 1, 3, 4), (0, 2, 7), (1, 3, 5), (1, 2, 6), (3, 7), (4, 6), (0, 3, 6), (2, 3, 4), (0, 4, 5), (0, 1, 2, 5)}
        
        so now we need to find 3 tuple sets which are mutually exclusive of each other, ie,
        ((0, 2, 7), (1, 3, 5), (4, 6)) -- each of these sums up to 12, and all of them combined make up the nums arr
        '''
        for c in combinations(self.soln, k):
            arr = []
            for tup in list(c):
                arr.extend(list(tup))
            if len(set(arr)) == len(nums):
                return True
            
        return False